from uuid import uuid4
from fastapi import FastAPI, File, UploadFile, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from PIL import Image
import io
import os
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from app.nn_models.Embed import QuestionAnsweringSystem
from app.nn_models.ImageClassifier import ImageClassifier
from app.helpers.ClassManager import ClassManager
from app.nn_models.YoloClassifier import YoloImageClassifier

class_manager = ClassManager()
class_names = class_manager.load_classes()

# Модель для входных данных
class PredictRequest(BaseModel):
    image_url: str

# Модель для входных данных
class AskRequest(BaseModel):
    question: str

# Загрузка модели
qa_system = QuestionAnsweringSystem(
        faiss_index_path="faiss_index"
    )
classifier = YoloImageClassifier(
    class_names=class_names
)

# Создание FastAPI приложения
app = FastAPI()

# Настройка CORS
# origins = [
#     "http://localhost:4200",
#     "https://localhost:4200",
#     "http://10.0.2.2:8000",
#     "https://10.0.2.2:8000",
# ]

# Добавление CORS в FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Настройка Jinja2
templates = Jinja2Templates(directory="app/templates")

# Папка для сохранения загруженных изображений
UPLOAD_DIR = "app/static"
os.makedirs(UPLOAD_DIR, exist_ok=True)
app.mount("/static", StaticFiles(directory=UPLOAD_DIR), name="static")

# # Главная страница с формой загрузки
@app.get("/", response_class=HTMLResponse)
async def upload_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Загрузка изображения
@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    try:
        # Читаем изображение
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data))

        # Сохраняем изображение на сервере
        filename = f"{uuid4()}.png"
        image_path = os.path.join(UPLOAD_DIR, filename)
        image.save(image_path)

        # Возвращаем информацию о загруженном изображении
        return JSONResponse(content={
            "filename": file.filename,
            "format": image.format,
            "size": {"width": image.width, "height": image.height},
            "image_url": f"/static/{filename}"
        })

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)


# Предсказание
@app.post("/predict")
async def predict(request: PredictRequest):
    try:
        # Открываем изображение
        file_path = request.image_url.lstrip("/")
        image_path = os.path.join("app", file_path)

        # Предсказание класса
        predicted_class = classifier.predict(image_path)

        # Возвращаем результат
        return JSONResponse(content={"predicted_class": predicted_class})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)


@app.post("/ask")
async def ask_question(request: AskRequest):
    try:
        # Ответ на вопрос
        answer = qa_system.ask_question(request.question)

        # Возвращаем результат
        return JSONResponse(content={
            "answer": answer,
        })
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)