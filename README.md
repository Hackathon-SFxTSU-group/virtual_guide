# Технологическая практика. Задача "Умный городской гид". Команда 14 ТГУ. Соцсеть ARnet

## 📝 Описание проекта

Arnet представляет собой социальную сеть с дополненной реальностью.
В Arnet присутсвует карта с геометками на объекты, представляющие собой
памятники, достопримечательности (в том числе здания и культурно и исторически значимые объекты),
а также экспонаты музеев.
Для присутсвующих в базе Arnet объектов можно получить сведения
наведня на них камеру (используя пользовательское приложение Arnet).
Так Arnet позволяет пользователю:
- узнать название и описание объекта;
- поспрашивать чат-бота про дополнительные сведения об объекте (например, про историю объекта);
- просмотреть, как меняли в AR (дополненной реальности) этот объект
другие пользователи (в том числе ознакомиться с фото, видео, аудио, комментарими
и голосовыми сообщеними от другиx пользователей, а также отфильтровать контент
по типу, AR/VR дополнения места,
- произвести наложение фото (видео) данного объекта в разном времени, например,
посмотреть как выглядил данный объект (место) зимой, летом или 10 лет назад.
- найти места, измененные в дополненной реальности другими пользователями, при помощи геометок

## 🎯 Основные цели

1. Цель 1: создать умный городской гид
2. Цель 2: на базе гида сформировать приложение с дополненной реальностью
3. Цель 3: масштабирвоать приложение. сделать полнофункциональную соцсеть с дополненной реальностью

## 👥 Наша команда

| Имя               | Роль                |
|-------------------|--------------------|
| Алексей Ширяев         | Тимлид. Планирование работ, протоколирование встреч, формирование БД обучающих данных (фото/видео, аугментация)             |
| Никита Холин         | выбор и дообучение нейросети, портирование на сервер            |
| Артём Низельский        | разработка мобильного приложения, интеграция с сервером           |
| Данила Краснов      | подготовка сервера, интеграция с мобильным приложением и нейросетью, GIT         |
| Михаил Молчанов       | формирование БД обучающих данных (фото/видео, аугментация)          |
| Владимир Паланцевич      | формирование БД обучающих данных (фото/видео, аугментация)          |
| Николай Курзенков      | формирование БД обучающих данных (фото/видео, аугментация)          |

---

## :date: Этапы работы

1. **Этап 1** Умный городской гид:
    - Выбор, обучение и внедрение в проект модели для распознования
(классификации) объектов;
    - Выбор модели для выдачи ответов на вопросы пользователя;
    - Создание серверного приложения для классификации объектов на изображениях
и выдачи ответов на вопросы пользователя;
    - Пополнение базы известных объектов (получение фотографий и текстовой
информации для выдачи ответов пользователям);
    - Разработка прототипа мобильного приложения для пользователей.
2. **Этап 2** Этап 2: AR соцсеть
   – работа с видеопотоком с камеры в реальном времени
   - наложение текстового описания на распознанный объект
   - возможность пользователю сделать пользовательское фото объекта и описание и загрузить его в общий доступ с геометкой
   - приложение распознает дубли загруженных фото и интегрирует их в общую БД
3. **Этап 3**  Масштабирование
   – добавление геометок
   - добавление возможности переписки
   - добавление возможности обмена контентом, комментирование

## 📂 Состав репозитория

```bash
📦 virtual_guide
├── 📁 app  ...................................  # Код серверной части проекта
├── 📁 frontend-app  ..........................  # Код пользовательского приложения
├── 📁 faiss_index  ...........................  # Актуальные (используемые) векторы
│                                                # для вопросно-ответной системы
├── 📁 saved_models  ..........................  # Актуальные (используемые) модели для
│                                                # классификации присылаемых изобаржений
├── 📁 preprocessing  .........................  # Скрипты для препроцессинга (подготовки
│                                                # исходных данных для обучения)
├── 📄 README.md  .............................  # Сведения о проекте (текущий файл)
├── 📄 RAG_for_question_and_answaring.ipynb  ..  # Ноутбук для формирования векторов
│                                                # для вопросно-ответной системы
├── 📄 resnet_train.ipynb  ....................  # Ноутбук для обучения модели resnet
├── 📄 vit_train.ipynb  .......................  # Ноутбук для обучения модели vit
├── 📄 yolo_train.ipynb  ......................  # Ноутбук для обучения моделй yolo
├── 📄 update_json.ipynb  ...................... # Ноутбук для обновления classes.json
├── 📄 classes.json  ..........................  # JSON-файл, содержащий перечень доступных
│                                                # для распознования классов
├── 📄 .gitignore  ............................  # Файл исключений Git
└── 📄 requirements.txt  ......................  # Зависимости для Python
```
---

## 📊 Состояние проекта

![Project Status](https://img.shields.io/badge/status-active-success.svg)

:white_check_mark: Создан протип кроссплатформенного мобильного приложения: 
- демонстрация работы с фото: https://drive.google.com/file/d/1ufyJyNCBtuWCCOpxrpkdEAwkhLVod1RQ/view?usp=sharing
- демонстрация работы с видео: https://drive.google.com/file/d/1JWqRe5Iz1wCYpx1kjtZ3XrKPSAoGTLWU/view?usp=sharing

:hammer: В работе: 
- работа с видеопотоком с камеры в реальном времени
- наложение текстового описания на распознанный объект
- возможность пользователю сделать пользовательское фото объекта и описание и загрузить его в общий доступ с геометкой
- приложение распознает дубли загруженных фото и интегрирует их в общую БД

