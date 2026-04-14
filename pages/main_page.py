import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    """
    PageObject для главной страницы Кинопоиска
    """

    SEARCH_INPUT = (By.CSS_SELECTOR,
                    "input[placeholder='Фильмы, сериалы, персоны']")

    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    SEARCH_RESULTS = (By.CSS_SELECTOR, "a[href*='/film/']")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Открыть сайт: {url}")
    def open(self, url: str) -> None:
        self.driver.get(url)

    @allure.step("Выполнить поиск фильма: {text}")
    def search_movie(self, text: str) -> None:
        search = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_INPUT)
        )
        search.clear()
        search.send_keys(text)

        search.submit()

    @allure.step("Проверить, что результаты поиска отображаются")
    def is_results_present(self) -> bool:
        elements = self.wait.until(
            EC.presence_of_all_elements_located(self.SEARCH_RESULTS)
        )
        return len(elements) > 0

    @allure.step("Открыть первый фильм из результатов")
    def open_first_movie(self) -> None:
        elements = self.wait.until(
            EC.presence_of_all_elements_located(self.SEARCH_RESULTS)
        )
        elements[0].click()

    @allure.step("Проверить, что открылась страница фильма")
    def is_movie_page_opened(self) -> bool:
        return "/film/" in self.driver.current_url
