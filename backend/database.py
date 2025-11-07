import sqlite3

last_where_clause = ''


def format_result(result: list):
    for i, item in enumerate(result):

        result[i] = {
                            'id': item[0], 'name': item[1], 'type': item[2], 'pokedex_number': item[3],
                            'hp': item[4], 'series': item[5], 'set_number': item[6],
                            'illustrator': item[7], 'release_year': item[8],
                            'attack_name': item[11], 'attack_damage': item[12], 'attack_effect': item[13]
                        }
    return result
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

    result = format_result(result)
    con.close()
    last_where_clause = ''
    return {'cards': result}


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

    last_where_clause = where_clause 
    return {'cards': result}
        


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

    result = format_result(result)

    con.close()
    last_where_clause = where_clause
    return {'cards': result}