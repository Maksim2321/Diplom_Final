import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from config import BASE_URL


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.ui
@allure.title("Поиск фильма")
def test_search_movie(driver):
    with allure.step("Открыть сайт"):
        driver.get(BASE_URL)

    with allure.step("Ввести фильм"):
        search = driver.find_element(By.NAME, "kp_query")
        search.send_keys("Интерстеллар")
        search.submit()

    with allure.step("Проверка результата"):
        assert "Интерстеллар" in driver.page_source


@pytest.mark.ui
@allure.title("Переход в карточку фильма")
def test_open_movie_card(driver):
    driver.get(BASE_URL)
    driver.find_element(By.NAME, "kp_query").send_keys("Матрица")
    driver.find_element(By.NAME, "kp_query").submit()

    movie = driver.find_element(By.CSS_SELECTOR, "a[href*='/film/']")
    movie.click()

    assert "Матрица" in driver.page_source


@pytest.mark.ui
@allure.title("Проверка рейтинга фильма")
def test_movie_rating(driver):
    driver.get(BASE_URL + "/film/326/")

    rating = driver.find_element(By.CLASS_NAME, "styles_ratingKpTop__8p7mM")
    assert rating.text != ""


@pytest.mark.ui
@allure.title("Проверка загрузки страницы")
def test_page_load(driver):
    driver.get(BASE_URL)
    assert driver.title != ""


@pytest.mark.ui
@allure.title("Проверка поиска пустого запроса")
def test_empty_search(driver):
    driver.get(BASE_URL)
    driver.find_element(By.NAME, "kp_query").submit()

    assert "ничего не найдено" in driver.page_source.lower()