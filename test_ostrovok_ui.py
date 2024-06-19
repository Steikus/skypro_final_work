from skypro_final_work.methods.MainPage import MainPage
from selenium import webdriver
import pytest
import allure


@allure.epic("UI-tests")
@allure.severity("blocker")
@pytest.fixture
def driver() -> MainPage:
    browser = webdriver.Chrome()
    browser.maximize_window()
    auth = MainPage(browser)
    yield auth
    browser.quit()


@allure.id("UI-1")
@allure.title("Регистрация нового пользователя")
@allure.description("Создание нового пользователя на случайную почту")
def test_registration_form(driver: MainPage):
    from faker import Faker
    fake = Faker()
    with allure.step("Сгенерировать случайную почту"):
        fakemail = fake.email()
    with allure.step("Отправить данные на регистрацию"):
        logname = driver.register(fakemail)
    assert fakemail == logname


@allure.id("UI-2")
@allure.title("Прохождение формы входа на сайт")
def test_login_form(driver: MainPage):
    with allure.step("Указать данные для входа на платформу"):
        email = "leheg32580@cnurbano.com"
        password = "WvIfT9i9uj6VuQH"
    with allure.step("Подтвердить вход на платформу"):
        driver.login(email, password)
    with allure.step("Получить логин из личного кабинета"):
        login = driver.get_login_from_orders()
    assert email == login


@allure.id("UI-3")
@allure.title("Поиск отелей на определённую дату и место")
@allure.description("Запрос на совпадение локации в поиске с искомой")
def test_hotel_search(driver: MainPage):
    with allure.step("Указать данные для поиска отеля: город и даты"):
        city = "Токио"
        data_in = "Aug 25 2024"
        data_out = "Aug 29 2024"
    with allure.step("Запустить поиск отелей по критериям"):
        driver.searching_for_hotel(city, data_in, data_out)
    with allure.step("Получить название города в списке отелей"):
        driver.search_results_city()
    assert city in driver.search_results_city()


@allure.id("UI-4")
@allure.title("Добавление отеля в избранное")
@allure.description("Добавление любого отеля из списка в избранное")
def test_add_hotel_to_favorite(driver: MainPage):
    with allure.step("Указать данные для поиска отеля"):
        city = "Токио"
        data_in = "Aug 25 2024"
        data_out = "Aug 29 2024"
    with allure.step("Запустить поиск отелей по критериям"):
        driver.searching_for_hotel(city, data_in, data_out)
    with allure.step("Перейти на страницу отеля через название"):
        driver.get_to_hotel_by_title(2)
    with allure.step("Получить название отеля со страницы"):
        add_name = driver.get_hotel_name()
    with allure.step("Добавить отель в изранное"):
        driver.add_to_favorite_page()
    with allure.step("Перейти в избранное"):
        driver.go_to_favorite()
    with allure.step("Получить информацию о названии в избранном"):
        fav_name = driver.get_favorite_hotel_name()
    assert add_name == fav_name


@allure.id("UI-5")
@allure.title("Добавление отеля в избранное")
@allure.description("Стоимость отеля на странице отелей совпадает со стоимостью в корзине")
def test_check_price(driver: MainPage):
    with allure.step("Указать данные для поиска отеля"):
        city = "Москва"
        data_in = "Aug 25 2024"
        data_out = "Aug 29 2024"
    with allure.step("Запустить поиск отелей по критериям"):
        driver.searching_for_hotel(city, data_in, data_out)
    with allure.step("Перейти на страницу отеля через кнопку"):
        driver.get_to_hotel_by_button(0)
    with allure.step("Получить информации о стоимости на странице отеля"):
        price_on_page = driver.get_price_go_check(0)
    with allure.step("Получить информацию о стоимости на странице бронирования"):
        price_of_reserve = driver.reserve_page_get_price()
    assert price_on_page == price_of_reserve
