from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://b2c.passport.rt.ru/')

    AUTORIZATION = (By.XPATH, "//h1[contains(text(),'Авторизация')]")
    LOGIN = (By.XPATH, "//div[@id='t-btn-tab-login']")
    USERNAME = (By.XPATH, "//input[@id='username']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    BUTTON = (By.XPATH, "//button[@id='kc-login']")
    BUTTON_LOGOUT = (By.CSS_SELECTOR, "#logout-btn")
    ERROR = (By.XPATH, "//span[@id='form-error-message']")
    REGISTRATION = (By.XPATH, "//a[@id='kc-register']")
    NAME = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input')
    SURNAME = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input')
    REGION = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/div/input')
    EMAIL = (By.XPATH, "//input[@id='address']")
    PASS = (By.XPATH, " //input[@id='password']")
    PASS_CONFIRM = (By.XPATH, "//input[@id='password-confirm']")
    BUTTON_REGIS = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/button')
    PAGE_RIGHT = (By.XPATH, '//*[@id="page-right"]/div/div/h1')
    ERROR_MESSAGE = (By.XPATH, "// span[contains(text(), 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXX')]")
    ERROR_MESSAGE_NAME = (By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")
    FORGOT_PASSWORD = (By.XPATH, '//a[@id="forgot_password"]')
    VK = (By.CSS_SELECTOR, '#oidc_vk>svg')
    LABLE_VK = (By.CSS_SELECTOR, '#install_allow')
    OK = (By.CSS_SELECTOR, '#oidc_ok>svg')
    LABLE_OK = (By.CSS_SELECTOR, '#widget-el>div.ext-widget_h>div')

