from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, status, Response
from fastapi.middleware.cors import CORSMiddleware

from database import get_all_cards, get_card_by_id
from database import get_cards_by_series, get_cards_by_type, get_cards_by_year
from database import add_card
from database import update_card
from database import delete_card_by_id
from database import search_cards



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
    name: str

#------------------------------
# GET routes
#------------------------------

# GET ALL
@app.get('/cards')
def get_cards():
    return {'response': get_all_cards()}

# GET ONE
@app.get('/card/id/{card_id}')
def get_card(response: Response, card_id: str):
    result = get_card_by_id(card_id)
    print(result)

    if not result:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'status': 'Not Found', 'message': 'Card with given id not found', 'response': None}

    return {'status': 'OK', 'response': result}

# 3 GET routes
@app.get('/cards/year/{release_year}')
def get_card(response: Response, release_year: str):
    result = get_cards_by_year(release_year)

    if not result:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'status': 'Not Found', 'message': 'Card from the given release year not found', 'response': None}

    return {'status': 'OK', 'response': result}

@app.get('/cards/type/{card_type}')
def get_card(response: Response, card_type: str):
    result = get_cards_by_type(card_type)

    if not result:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'status': 'Not Found', 'message': 'Cards with given type not found', 'response': None}

    return {'status': 'OK', 'response': result}

@app.get('/cards/series/{series}')
def get_card(response: Response, series: str):
    result = get_cards_by_series(series)

    if not result:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'status': 'Not Found', 'message': 'Cards from given series not found', 'response': None}
    return {'status': 'OK', 'response': result}

#------------------------------------
# POST route
#------------------------------------

@app.post('/card/add')
def post_add_card(response: Response, card: CardAdd):
    result = add_card(card)
    if result['status'] == 'Error':
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'status': 'Bad Request', 'message': 'Malformed card creation request', 'response': None}
    return {'status': 'OK', 'response': result['card']}

#------------------------------------
# PUT route
#------------------------------------

@app.put('/card/update/{card_id}/name')
def put_update(card_id: str, response: Response, request: CardUpdateRequest):
    result = update_card(card_id, request.name)
    if result['status'] == 'Success':
        response.status_code = status.HTTP_201_CREATED
        return {'status': 'OK', 'response': result['card']}
    elif result['status'] == 'Failed':
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'status': 'Not Found', 'message': 'Card with given id not found', 'response': None}
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'status': 'Bad Request', 'message': 'Malformed request', 'response': None}



#----------------------------------
# DELETE route
#----------------------------------

@app.delete('/card/delete/{card_id}')
def delete_card(response: Response, card_id: str):
    result = delete_card_by_id(card_id)
    if result['status'] == 'Error':
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'status': 'Not Found', 'message': 'Card with given id not found', 'response': None}
    else:
        return {'status': 'OK', 'response': result['card']}


#----------------------------------
# POST card search (OLD
#----------------------------------
@app.post('/search_cards')
def post_cards(request: CardSearch):
    result = search_cards(request.column, request.value)
    print(result)
    return result