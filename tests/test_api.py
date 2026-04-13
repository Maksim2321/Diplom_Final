import pytest
import requests
import allure
from config import API_URL, API_KEY

headers = {
    "X-API-KEY": API_KEY
}


@pytest.mark.api
@allure.title("Поиск фильма API")
def test_search_movie_api():
    response = requests.get(
        f"{API_URL}/movie/search",
        headers=headers,
        params={"query": "Интерстеллар"}
    )

    assert response.status_code == 200
    assert "docs" in response.json()
