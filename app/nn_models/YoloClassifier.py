import torch
from torchvision import models, transforms
from PIL import Image
from ultralytics import YOLO


class YoloImageClassifier:
    def __init__(self, class_names: list, model_path: str = "saved_models/yolo_best.pt", ):
        """
        Инициализация классификатора изображений.

        :param model_path: Путь к файлу с весами модели.
        :param class_names: Список классов для предсказания.
        """
        self.class_names = class_names

        # Загрузка модели
        self.model = YOLO(model_path)  

    def predict(self, image_path: str):
        """
        Предсказание класса для изображения.

        :param image_path: Путь к изображению.
        :return: Предсказанный класс.
        """
        try:
            # Открываем изображение
            results = self.model.predict(source=image_path)

            predicted_class_index = results[0].probs.top1
            predicted_class = results[0].names[predicted_class_index]
            return predicted_class

        except Exception as e:
            raise ValueError(f"Ошибка при предсказании: {e}")