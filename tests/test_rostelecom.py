from pages.main_page import MainPage
from settings import *
from time import sleep


#  1) Заголовок "Авторизация" отображен на странице
def test_autorization_is_visible(driver):
    main_page = MainPage(driver)
    autorization = main_page.is_visible(MainPage.AUTORIZATION)
    assert autorization == True


#   2) Кнопка "Логин" кликабельна и по ее нажатию открывается форма авторизации с полем "Логин"
def test_login_is_clicable(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.LOGIN)
    login_button = main_page.is_visible(MainPage.USERNAME)
    assert login_button == True


#    3) Проверка позитивного сценария авторизации по почте
def test_valid_data_mail(driver):
    main_page = MainPage(driver)
    main_page.input_data(MainPage.USERNAME, valid_email)
    main_page.input_data(MainPage.PASSWORD, valid_password)
    sleep(10)  # чтобы ввести на случай необходимости вручную капчу
    main_page.find_element_and_click(MainPage.BUTTON)
    element = main_page.is_visible(MainPage.BUTTON_LOGOUT)
    assert element == True


#    4) Авторизация по валидной почте и невалидному паролю (негативный сценарий авторизации)
def test_invalid_pass_mail(driver):
    main_page = MainPage(driver)
    main_page.input_data(MainPage.USERNAME, valid_email)
    main_page.input_data(MainPage.PASSWORD, invalid_password)
    main_page.find_element_and_click(MainPage.BUTTON)
    error_button = main_page.is_visible(MainPage.ERROR)
    assert error_button == True


#    5) Авторизация по невалидной почте и валидному паролю (негативный сценарий авторизации)
def test_invalid_email(driver):
    main_page = MainPage(driver)
    main_page.input_data(MainPage.USERNAME, invalid_email)
    main_page.input_data(MainPage.PASSWORD, valid_password)
    main_page.find_element_and_click(MainPage.BUTTON)
    error_button = main_page.is_visible(MainPage.ERROR)
    assert error_button == True


#    6) Авторизация по невалидной почте и невалидному паролю (негативный сценарий авторизации)
def test_invalid_data(driver):
    main_page = MainPage(driver)
    main_page.input_data(MainPage.USERNAME, invalid_email)
    main_page.input_data(MainPage.PASSWORD, invalid_password)
    main_page.find_element_and_click(MainPage.BUTTON)
    error_button = main_page.is_visible(MainPage.ERROR)
    assert error_button == True


#    7) Кнопка "Зарегистрироваться" кликабельна и открывает форму "Регистрация"
def test_check_in(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    check = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert check == BaseUrl.CHECK_IN


#  8) Заполнение формы "Регистрация" и проверка кликабельности кнопки "Зарегистрироваться" (позитивный сценарий)
def test_check_in_and_registration(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME, name)
    main_page.input_data(MainPage.SURNAME, surname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.EMAIL, email)
    main_page.input_data(MainPage.PASS, password)
    main_page.input_data(MainPage.PASS_CONFIRM, password)
    main_page.find_element_and_click(MainPage.BUTTON_REGIS)
    regist = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert regist == BaseUrl.CONFIRM_EMAIL


#    9) Заполнение формы "Регистрация" с невалидным мобильным телефоном (на 3 цифры больше, негативный сценарий)
def test_check_in_with_invalid_mobile(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME, name)
    main_page.input_data(MainPage.SURNAME, surname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.EMAIL, invalid_mobile)
    main_page.input_data(MainPage.PASS, password)
    main_page.input_data(MainPage.PASS_CONFIRM, password)
    main_page.find_element_and_click(MainPage.BUTTON_REGIS)
    invalid_regist = main_page.get_text_of_element(MainPage.ERROR_MESSAGE)
    assert invalid_regist == BaseUrl.EMAIL_INVALID


#    10) Заполнение формы "Регистрация" с невалидным именем (менее 2 символов, негативный сценарий)
def test_check_in_with_invalid_name(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME, invalid_name)
    main_page.input_data(MainPage.SURNAME, surname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.EMAIL, email)
    main_page.input_data(MainPage.PASS, password)
    main_page.input_data(MainPage.PASS_CONFIRM, password)
    main_page.find_element_and_click(MainPage.BUTTON_REGIS)
    invalid_regist_name = main_page.get_text_of_element(MainPage.ERROR_MESSAGE_NAME)
    assert invalid_regist_name == BaseUrl.NAME_INVALID


#    11) Заполнение формы "Регистрация" с валидным именем (2 символа кириллицей, позитивный сценарий)
def test_check_in_with_valid_name(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME, valid_name)
    main_page.input_data(MainPage.SURNAME, surname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.EMAIL, email)
    main_page.input_data(MainPage.PASS, password)
    main_page.input_data(MainPage.PASS_CONFIRM, password)
    main_page.find_element_and_click(MainPage.BUTTON_REGIS)
    valid_regist_name = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert valid_regist_name == BaseUrl.CONFIRM_EMAIL


#    12) Заполнение формы "Регистрация" с валидным именем (30 символов кириллицей, позитивный сценарий)
def test_check_with_valid_name(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME, valid_name_max)
    main_page.input_data(MainPage.SURNAME, surname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.EMAIL, email)
    main_page.input_data(MainPage.PASS, password)
    main_page.input_data(MainPage.PASS_CONFIRM, password)
    main_page.find_element_and_click(MainPage.BUTTON_REGIS)
    valid_regist_name = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert valid_regist_name == BaseUrl.CONFIRM_EMAIL


#    13) Заполнение формы "Регистрация" с валидным именем (31 символ кириллицей, негативный сценарий)
def test_check_with_invalid_name(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.REGISTRATION)
    main_page.input_data(MainPage.NAME, thirty_one_letters_name)
    main_page.input_data(MainPage.SURNAME, surname)
    main_page.input_data(MainPage.REGION, region)
    main_page.input_data(MainPage.EMAIL, email)
    main_page.input_data(MainPage.PASS, password)
    main_page.input_data(MainPage.PASS_CONFIRM, password)
    main_page.find_element_and_click(MainPage.BUTTON_REGIS)
    invalid_reg = main_page.get_text_of_element(MainPage.ERROR_MESSAGE_NAME)
    assert invalid_reg == BaseUrl.NAME_INVALID


#    14) Кнопка "Забыл пароль" кликабельна и открывает форму "Восстановление пароля"
def test_forgot_passwort(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.FORGOT_PASSWORD)
    fog_passw = main_page.get_text_of_element(MainPage.PAGE_RIGHT)
    assert fog_passw == BaseUrl.FOG_PASSWORD


#    15) Кнопка "VK" кликабельна, и открывает форму для регистрации через аккаунт ВКонтакте
def test_vk_is_available(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click(MainPage.VK)
    vk_avail = main_page.get_text_of_element(MainPage.LABLE_VK)
    assert vk_avail == BaseUrl.ENTRY_VK


#   16) Кнопка "ОК" кликабельна, и открывает форму для регистранции через аккаунт "Одноклассники"
def test_ok_is_available(driver):
    main_page = MainPage(driver)
    main_page.find_element_and_click((MainPage.OK))
    ok_avail = main_page.get_text_of_element(MainPage.LABLE_OK)
    assert ok_avail == BaseUrl.OK














