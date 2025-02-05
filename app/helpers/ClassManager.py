import os
import json

class ClassManager:
    def __init__(self, train_dir=None, json_path=None):
        self.base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

        self.train_dir = train_dir or os.path.join(self.base_dir, "images/train")
        self.json_path = json_path or os.path.join(self.base_dir, "classes.json")

    def update_json(self):
        """Сканирует train и обновляет classes.json"""
        if not os.path.exists(self.train_dir):
            raise FileNotFoundError(f"Папка {self.train_dir} не найдена!")

        # Получаем список всех папок-классов
        class_names = [d for d in os.listdir(self.train_dir) if os.path.isdir(os.path.join(self.train_dir, d))]

        # Записываем в JSON
        with open(self.json_path, "w", encoding="utf-8") as f:
            json.dump({"class_names": class_names}, f, ensure_ascii=False, indent=4)

        print(f"✅ Обновлено {self.json_path} с {len(class_names)} классами.")

    def load_classes(self):
        """Загружает классы из JSON"""
        if not os.path.exists(self.json_path):
            raise FileNotFoundError(f"Файл {self.json_path} не найден! Запусти update_json() сначала.")

        with open(self.json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        class_names = data.get("class_names", [])
        if not class_names:
            raise ValueError("Файл classes.json пустой или поврежден!")

        return class_names
