import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.main_page import MainPage
from config import BASE_URL


@pytest.fixture
def driver() -> WebDriver:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.ui
@allure.title("Поиск фильма")
@allure.story("Поиск")
def test_search_movie(driver: WebDriver) -> None:
    page = MainPage(driver)

    with allure.step("Открыть сайт"):
        page.open(BASE_URL)

    with allure.step("Выполнить поиск"):
        page.search_movie("Интерстеллар")

    with allure.step("Проверка результатов"):
        assert "Интерстеллар" in driver.page_source
