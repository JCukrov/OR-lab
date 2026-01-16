import sqlite3

last_where_clause = ''

# HELPER

def format_result(result: list):
    for i, item in enumerate(result):
        result[i] = {
                "@context": {
                    "@vocab": "https://schema.org/",
                    "name": "name",
                    "release_year": "releaseDate"
                },
                "@type": "Product",
                'id': item[0], 'name': item[1], 'type': item[2], 'pokedex_number': item[3],
                'hp': item[4], 'series': item[5], 'set_number': item[6],
                'illustrator': item[7], 'release_year': item[8],
                'attack_name': item[11], 'attack_damage': item[12], 'attack_effect': item[13]
        }
    return result


#----------------------------------------
# GET CARDS
#----------------------------------------

#GET all
def get_all_cards():
    global last_where_clause
    con = sqlite3.connect('./data/database.db')
    cur = con.cursor()
    query = '''
    SELECT *
    FROM cards
    JOIN attacks
    ON attacks.card_id = cards.id
    '''
    result = cur.execute(query).fetchall()

    con.close()

    result = format_result(result)
    last_where_clause = ''
    return result

#GET one
def get_card_by_id(id: str) -> dict:
    con = sqlite3.connect('./data/database.db')
    cur = con.cursor()
    query = '''
    SELECT *
    FROM cards
    JOIN attacks
    ON attacks.card_id = cards.id
    WHERE cards.id = ?
    GROUP BY cards.id
    '''
    result = cur.execute(query, [id]).fetchall()

    con.close()

    print(result)
    if result == []:
        return None
    return format_result(result)[0]

# 3 GET routes
def get_cards_by_type(card_type: str) -> dict:
    con = sqlite3.connect('./data/database.db')
    cur = con.cursor()
    query = '''
    SELECT *
    FROM cards
    JOIN attacks
    ON attacks.card_id = cards.id
    WHERE cards.type = ?
    GROUP BY cards.id
    '''
    result = cur.execute(query, [card_type]).fetchall()

    con.close()

    if result == []:
        return None

    return format_result(result)

def get_cards_by_year(release_year: str) -> dict:
    con = sqlite3.connect('./data/database.db')
    cur = con.cursor()
    query = '''
    SELECT *
    FROM cards
    JOIN attacks
    ON attacks.card_id = cards.id
    WHERE cards.release_year = ?
    GROUP BY cards.id
    '''
    result = cur.execute(query, [release_year]).fetchall()

    con.close()

    if result == []:
        return None
    return format_result(result)

def get_cards_by_series(series: str) -> dict:
    con = sqlite3.connect('./data/database.db')
    cur = con.cursor()
    query = '''
    SELECT *
    FROM cards
    JOIN attacks
    ON attacks.card_id = cards.id
    WHERE cards.series = ?
    GROUP BY cards.id
    '''
    result = cur.execute(query, [series]).fetchall()

    con.close()

    if result == []:
        return None
    return format_result(result)

#----------------------------------------
# ADD CARD
#----------------------------------------
def add_card(card: dict):
    con = sqlite3.connect('./data/database.db')
    cur = con.cursor()
    try:
        query = '''
        INSERT INTO cards(name, type, pokedex_number, hp, series, set_number, illustrator, release_year)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        cur.execute(query, [card.name, card.card_type, card.pokedex_number, card.hp, card.series, card.set_number, card.illustrator, card.release_year])
        
        card_id = cur.lastrowid

        query = '''
        INSERT INTO attacks(card_id, name, damage, effect)
        VALUES (?, ?, ?, ?)
        '''
        cur.execute(query, [card_id, card.attack_name, card.attack_damage, card.attack_effect])
        con.commit()
        con.close()
    except:
        return {'status': 'Error'}
    return{'status': 'Success', 'id': card_id, 'card': get_card_by_id(card_id)}


#---------------------------------------------------
# UPDATE CARDS
#---------------------------------------------------

def update_card(id: str, newName: str):
    con = sqlite3.connect('./data/database.db')
    cur = con.cursor()
    query = '''
    UPDATE cards
    SET name = ?
    WHERE cards.id = ?
    '''
    try:
        cur.execute(query, [newName, id])
        con.commit()
        con.close()
        return {'status': 'Success', 'card': get_card_by_id(id)}
    except:
        return {'status': 'Failed', 'card': None}

#---------------------------------------------------
# DELETE CARDS
#---------------------------------------------------

def delete_card_by_id(card_id: str):
    con = sqlite3.connect('./data/database.db')
    cur = con.cursor()
    card = get_card_by_id(card_id)
    if card == None:
        return {'status': "Error", 'card': None}

    query = '''
    DELETE FROM cards
    WHERE id = ?
    '''
    try:
        cur.execute(query, [card_id])
        con.commit()
        con.close()
        return {'status':'Success', 'card': card}
    except Exception(e):
        print(e)
        return {'status': 'Error', 'card': None}

#-----------------------------------------
# SEARCH FILTERING
#-----------------------------------------

def search_all_columns(columns, value):
    global last_where_clause
    con = sqlite3.connect('./data/database.db')
    cur = con.cursor()

    where_clause = " OR ".join([f"{column} LIKE ?" for column in columns])

    query = f'''
    SELECT *
    FROM cards
    JOIN attacks
    ON attacks.card_id = cards.id
    WHERE {where_clause}
    '''
    params = [f'%{value}%' for _ in columns]
    result = cur.execute(query, params).fetchall()

    result = format_result(result)

    con.close()

    last_where_clause = where_clause 
    return result
        


def search_cards(column, value):
    global last_where_clause
    con = sqlite3.connect('./data/database.db')
    cur = con.cursor()

    columns = ['cards.name', 'type', 'pokedex_number',
        'hp', 'series', 'set_number',
        'illustrator', 'release_year', 'attacks.name',
        'attacks.damage', 'attacks.effect'
    ]
    match column:
        case 'name':
            column = 'cards.name'
        case 'attack_name':
            column = 'attacks.name'
        case 'attack_damage':
            column = 'attacks.damage'
        case 'attack_effect':
            column = 'attacks.effect'
        case 'all':
            return search_all_columns(columns, value)
            
    where_clause = f'{column} LIKE ?'
    query = f'''
    SELECT *
    FROM cards
    JOIN attacks
    ON attacks.card_id = cards.id
    WHERE {column} LIKE ?
    '''
    result = cur.execute(query, [f'%{value}%']).fetchall()

    con.close()

    result = format_result(result)

    last_where_clause = where_clause
    return result