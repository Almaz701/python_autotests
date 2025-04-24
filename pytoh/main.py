import requests

# Ваши данные (замените на реальные)
token = "d68ba5c0ca6c038c48376eb4d24b291c"
trainer_id = "35172"
base_url = "https://api.pokemonbattle.ru/v2"

# 1. Создание покемона (POST /pokemons)
headers = {
    "Content-Type": "application/json",
    "trainer_token": token
}

body = {
    "name": "Бульбазавр",
    "photo_id": 8
}

response_create = requests.post(
    f'{base_url}/pokemons', 
    headers=headers, 
    json=body
)

# Проверка и обработка ответа
if response_create.status_code == 201:
    print("Успешный ответ:")
    print(response_create.json())
    
