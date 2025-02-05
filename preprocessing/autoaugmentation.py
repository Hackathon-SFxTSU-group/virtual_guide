# Модули для аугментации
import torch
from torchvision.transforms import v2

# Модули для работы с файловой системой
from PIL import Image
import PIL
import sys
import os
from pathlib import Path

# Progress bar для отслеживания прогресса аугментации
from progress.bar import IncrementalBar


def autoaugmentation():
    '''Функция для автоматической аугментации изображений.

    Аргументы командной строки:
    src - директория с исходными изображениями (директория может
    содержать поддиректории с изображениями);
    dst - директория, в которой будут сохраняться аугментированные и
    копии исходных изображений, при этом все пути сохраняются как
    в оригинальной директории src;
    num [num = 10 по умолчанию] - опциональный аргумент, определяющий
    количество размножений изображения после аугментации
    (исходное изображение также считается, соответсвенно количество
    аугментаций составляет num-1).

    Возвращаемые данные:
    функция ничего не возвращает.
    '''
    if len(sys.argv) < 3:  # src и dst не переданы?
        print(f"Use: {sys.argv[0]} src dst num")
        exit()
    elif len(sys.argv) == 4:  # num передан?
        # Количество создаваемых аугментатором изображений
        number_augmentations = int(sys.argv[3])  # Значение из аргумента num
    else:
        # Количество создаваемых аугментатором изображений
        number_augmentations = 10  # Значение по умолчанию

    src = Path(sys.argv[1])  # Исходная директория с видефайлами
    dst = Path(sys.argv[2])  # Целевая директория для сохранения кадров

    # Объект для выполнения автоматической аугментации
    augmenter = v2.AutoAugment()

    # Инициализация Progress bar
    progress_cnt = 0  # Счетчик для инициализации Progress bar
    # Холостой проход по всем путям для подсчета файлов
    for full_path in src.rglob("*"):
        _, ext = os.path.splitext(full_path)
        # Проверка: длина расширения не более 5 символов (с учетом точки)?
        if ext != '' and len(ext) <= 5:
            progress_cnt += 1
    # Создание объекта Progress bar
    progress_bar = IncrementalBar("Augmented progress", max = progress_cnt)

    skipped_cnt = 0  # Счетчик пропущенных файлов
    total_images = 0  # Общий счетчик успешно сохраненных изображений

    # Перебор всех путей до всех файлов и директорий вложенных в src
    for full_path in src.rglob("*"):
        # Выделение пути директории и имени файла
        base, ext = os.path.splitext(full_path)
        # Взятие пути, не содержащего возвраты в предыдущие директории
        res_base = base.replace("../", '', -1)
        if len(ext) > 5:  # Длина ext > 5? - значит имя директории
        # содержит точку (или точки) и часть имени, ложно определенную как ext
        # необходимо вернуть обратно в имя директории.
            res_base = res_base + ext
        # Если полный путь содержит имя файла, а не директории
        if ext != '' and len(ext)<=5:
            # Аугментация и сохранение изображений
            try:
                orig_img = Image.open(Path(full_path))  # Импорт изображения
                # Конвертация в RGB для исключения ошибок при аугментации
                orig_img = orig_img.convert("RGB")
            except PIL.UnidentifiedImageError:
                # Пропуск текущей итерации, если изображение
                # не было импортировано.
                progress_bar.next()  # Обновление Progress bar
                sys.stderr.write(f"\nFile: \"{full_path}\" was skipped\n")
                skipped_cnt += 1
                continue
            except:
                print(f"{full_path}, {ext}")
                continue
            # Генерация аугментированных изображений
            imgs = [
                # Количество аугментаций на 1 меньше, чем задано аргументом
                # num на входе функции (для того, чтобы итоговых изображений
                # вместе с оригинальным было также num экземпляров)
                augmenter(orig_img) for _ in range(number_augmentations-1)
            ]
            # Добавление в список imgs оригинального изображения
            imgs.insert(0, orig_img)
            # Сохранение оригинального и созданных аугментатором изображений
            for idx, img in enumerate(imgs):
                img.save(f"{dst}/{res_base}_{idx}.{ext}")
                total_images += 1
            progress_bar.next()  # Обновление Progress bar
        else:  # Полный путь содержит имя только директории
            # Проверка: поддиректория не создана?
            if not os.path.exists(f"{dst}/{res_base}"):
                # Cоздать поддиректорию
                os.makedirs(f"{dst}/{res_base}", exist_ok=False)
    progress_bar.finish()  # Завершение заполнения  Progress bar
    print(f"Augmented files: {progress_cnt-skipped_cnt} of {progress_cnt}")
    if skipped_cnt > 0:
        print(f"Skipped files: {skipped_cnt}")
    print(f"Total images after augmentation: {total_images}")


if __name__ == "__main__":
    autoaugmentation()
