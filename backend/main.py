import sqlite3

from fastapi import FastAPI
from database import get_all_cards, search_cards
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

class CardSearch(BaseModel):
    column: str
    value: str

@app.get('/cards')
def get_cards():
    return get_all_cards()

@app.post('/cards')
def post_cards(request: CardSearch):
    result = search_cards(request.column, request.value)
    print(result)
    return result

