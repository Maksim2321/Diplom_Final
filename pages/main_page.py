from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    # локаторы
    SEARCH_INPUT = (By.NAME, "kp_query")
    MOVIE_LINK = (By.CSS_SELECTOR, "a[href*='/film/']")

    def open(self, url: str) -> None:
        self.driver.get(url)

    def search_movie(self, text: str) -> None:
        search = self.driver.find_element(*self.SEARCH_INPUT)
        search.clear()
        search.send_keys(text)
        search.submit()

    def open_first_movie(self) -> None:
        movie = self.driver.find_element(*self.MOVIE_LINK)
        movie.click()
