import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome('C:/skillfactory/chromedriver.exe')
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    driver.quit()

