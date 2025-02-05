import torch
from torchvision import models, transforms
from PIL import Image


class ImageClassifier:
    def __init__(self, model_path: str, class_names: list):
        """
        Инициализация классификатора изображений.

        :param model_path: Путь к файлу с весами модели.
        :param class_names: Список классов для предсказания.
        """
        self.class_names = class_names

        # Загрузка модели
        self.model = models.resnet18(weights=None)  # Не загружаем предобученные веса
        num_ftrs = self.model.fc.in_features
        self.model.fc = torch.nn.Linear(num_ftrs, len(self.class_names))  # Заменяем последний слой

        # Загружаем веса модели
        state_dict = torch.load(model_path, map_location=torch.device('cpu'), weights_only=True)
        self.model.load_state_dict(state_dict)

        # Преобразования для изображений
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),  # Изменение размера изображений
            transforms.ToTensor(),          # Преобразование в тензор
            transforms.Normalize(           # Нормализация
                mean=[0.485, 0.456, 0.406], # Средние значения для ImageNet
                std=[0.229, 0.224, 0.225]   # Стандартные отклонения для ImageNet
            )
        ])

        # Переключаем модель в режим оценки
        self.model.eval()

    def predict(self, image_path: str):
        """
        Предсказание класса для изображения.

        :param image_path: Путь к изображению.
        :return: Предсказанный класс.
        """
        try:
            # Открываем изображение
            image = Image.open(image_path).convert('RGB')

            # Применение преобразований
            image = self.transform(image).unsqueeze(0)  # Добавляем batch dimension

            # Предсказание
            with torch.no_grad():
                output = self.model(image)
                _, predicted = torch.max(output, 1)
                predicted_class = self.class_names[predicted.item()]

            return predicted_class

        except Exception as e:
            raise ValueError(f"Ошибка при предсказании: {e}")