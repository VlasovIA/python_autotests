import requests

HOST = 'https://api.pokemonbattle-stage.me:9101'
token = '9ae491f26865510383df4f9938abfce4'
pokemon_id = '1893'

# Запрос на создание покемонв
responce = requests.post(url=f'{HOST}/pokemons', json={
                        'name': 'Бульбазавр',
                        'photo': 'https://dolnikov.ru/pokemons/albums/001.png'
                        },
                        headers={'Content-types': 'application/json',
                                 'trainer_token': f'{token}'})

print(responce.status_code, responce.reason, responce.text)

# Запрос на изменение имени покемона
responce = requests.put(url=f'{HOST}/pokemons', json={
                        'pokemon_id': f'{pokemon_id}',
                        'name': 'Ilya',
                        'photo': 'https://dolnikov.ru/pokemons/albums/008.png'
                        },
                        headers={'Content-types':'application/json',
                                 'trainer_token': f'{token}'})

print(responce.status_code, responce.reason, responce.text)

# Запрос на добаление покемона в покебол
responce = requests.post(url=f'{HOST}/trainers/add_pokeball', json={
                        'pokemon_id': f'{pokemon_id}'
                        },
                        headers={'Content-types': 'application/json',
                                 'trainer_token': f'{token}'})

print(responce.status_code, responce.reason, responce.text)