from fastapi import FastAPI

from database import get_all_cards, get_card_by_id
from database import get_cards_by_series, get_cards_by_type, get_cards_by_year
from database import add_card
from database import update_card
from database import delete_card_by_id
from database import search_cards

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

class CardAdd(BaseModel):
    name: str
    card_type: str
    pokedex_number: int
    hp: int
    series: str
    set_number: int
    illustrator: str
    release_year: int
    attack_name: str
    attack_damage: int
    attack_effect: str

class CardUpdateRequest(BaseModel):
    fields: [int]
    values: [int]

#------------------------------
# GET routes
#------------------------------

# GET ALL
@app.get('/cards')
def get_cards():
    return get_all_cards()

# GET ONE
@app.get('/card/id/{card_id}')
def get_card(card_id: str):
    return get_card_by_id(card_id)

# 3 GET routes
@app.get('/card/year/{release_year}')
def get_card(release_year: str):
    return get_cards_by_year(release_year)

@app.get('/card/type/{card_type}')
def get_card(card_type: str):
    return get_cards_by_type(card_type)

@app.get('/card/series/{series}')
def get_card(series: str):
    return get_cards_by_series(series)

#------------------------------------
# POST route
#------------------------------------

@app.post('/add_card')
def post_add_card(card: CardAdd):
    result = add_card(card)

#------------------------------------
# PUT route
#------------------------------------

@app.put('/update/{card_id}')
def put_update(card_id: str, request: CardUpdateRequest):
    result = update_card(card_id, request)
    return result


#----------------------------------
# DELETE route
#----------------------------------

@app.delete('/delete/{card_id}')
def delete_card(card_id: str):
    delete_card_by_id(card_id)


#----------------------------------
# POST card search (OLD
#----------------------------------
@app.post('/search_cards')
def post_cards(request: CardSearch):
    result = search_cards(request.column, request.value)
    print(result)
    return result


