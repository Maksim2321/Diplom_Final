import pytest
import requests
import allure
from config import API_URL, API_KEY

HEADERS: dict = {
    "X-API-KEY": API_KEY
}


@pytest.mark.api
@allure.title("Поиск фильма")
@allure.story("API Поиск")
def test_search_movie_api() -> None:
    with allure.step("Отправить запрос"):
        response = requests.get(
            f"{API_URL}/movie/search",
            headers=HEADERS,
            params={"query": "Интерстеллар"}
        )

    with allure.step("Проверка ответа"):
        assert response.status_code == 200


@pytest.mark.api
@allure.title("Фильм по ID")
@allure.story("API Фильм")
def test_get_movie_by_id() -> None:
    response = requests.get(f"{API_URL}/movie/301", headers=HEADERS)
    assert response.status_code == 200


@pytest.mark.api
@allure.title("Неверный API ключ")
@allure.story("API Ошибки")
def test_invalid_api_key() -> None:
    response = requests.get(
        f"{API_URL}/movie/301",
        headers={"X-API-KEY": "wrong"}
    )
    assert response.status_code == 401


@pytest.mark.api
@allure.title("Несуществующий ID")
@allure.story("API Ошибки")
def test_invalid_movie_id() -> None:
    response = requests.get(f"{API_URL}/movie/9999999", headers=HEADERS)
    assert response.status_code in [404, 400]


@pytest.mark.api
@allure.title("Поиск пустой строки")
@allure.story("API Поиск")
def test_empty_search() -> None:
    response = requests.get(
        f"{API_URL}/movie/search",
        headers=HEADERS,
        params={"query": ""}
    )
    assert response.status_code in [200, 400]


@pytest.mark.api
@allure.title("Поиск на русском")
@allure.story("API Поиск")
def test_search_russian() -> None:
    response = requests.get(
        f"{API_URL}/movie/search",
        headers=HEADERS,
        params={"query": "Матрица"}
    )
    assert response.status_code == 200


@pytest.mark.api
@allure.title("Проверка структуры ответа")
@allure.story("API Контракт")
def test_response_structure() -> None:
    response = requests.get(f"{API_URL}/movie/301", headers=HEADERS)
    data = response.json()

    assert "name" in data
    assert "year" in data


@pytest.mark.api
@allure.title("Метод без параметров")
@allure.story("API Ошибки")
def test_no_params() -> None:
    response = requests.get(f"{API_URL}/movie/search", headers=HEADERS)
    assert response.status_code in [200, 400]
