import requests
import pytest

base_url = "https://api.pokemonbattle.ru/v2/"  # Обновите URL
trainer_id = "35172"  # Замените на реальный ID

def test_get_trainers_status_code():
    response = requests.get(
        f'{base_url}/api/v2/trainers',
        params={"trainer_id": trainer_id},
        timeout=5
    )
    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}. Ответ: {response.text}"

def test_trainer_name_in_response():
    response = requests.get(
        f'{base_url}/api/v2/trainers',
        params={"trainer_id": trainer_id},
        timeout=5
    )
    data = response.json()
    assert data["trainer_name"] == "ИГОРЯН", f"Имя тренера не совпадает. Ответ: {data}"