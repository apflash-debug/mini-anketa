from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

questions = [
    {"id": 1, "text": "Как вас зовут?"},
    {"id": 2, "text": "Сколько вам лет?"},
    {"id": 3, "text": "Какой ваш любимый язык программирования?"},
    {"id": 4, "text": "Почему вы изучаете программирование?"},
]

answers_storage = []

class AnswerSet(BaseModel):
    answers: list[dict]

@app.get("/questions")
def get_questions():
    return questions

@app.post("/answers")
def post_answers(data: AnswerSet):
    answers_storage.append(data.answers)
    return {"message": "Спасибо!"}