from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Найти элемент и кликнуть по нему
    def find_element_and_click(self, locator, time=5):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator)).click()

    # Проверить видимость элемента
    def is_visible(self, locator, time=5) -> bool:
        element = WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        return bool(element)

    # Ввод данных
    def input_data(self, locator, text, time=5):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator)).send_keys(text)

    # Получить атрибут текст элемента
    def get_text_of_element(self, locator, time=5):
        element = WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        return element.text

