from skypro_final_work.methods.ApiRequests import ApiRequests
from faker import Faker
import allure


api = ApiRequests("https://ostrovok.ru/")
@allure.epic("UI-tests")
@allure.severity("blocker")


@allure.id("API-1")
@allure.title("Регистрация нового пользователя")
@allure.description("Создание нового пользователя на случайную почту")
def test_registration_form():
    fake = Faker()
    with allure.step("Сгенерировать случайную почту"):
        email = fake.email()
    with allure.step("Подтвердить регистрацию на платформе"):
        result = api.registration_form(email)
    assert result["message"] == "Спасибо, что зарегистрировались у нас на сайте!"


@allure.id("API-2")
@allure.title("Отображение популярных отелей в указанном регионе")
@allure.description("Получение списка популярных отелей по указанному региону")
def test_popular_hotels():
    with allure.step("Указание интересующего региона"):
        region = "Дубай"
    with allure.step("Получение списка популярных отелей"):
        result = api.top_hotels_for_region(region)
    assert result["hotels"][0]["region_name"] == region


@allure.id("API-3")
@allure.title("Получение информации о конкретном отеле")
def test_get_hotel_link():
    with allure.step("Указание интересующего отеля по его id"):
        hotel_name = "berezka_hotel"
    with allure.step("Получение короткой информации об отеле"):
        hotel_link = api.small_info_about_hotel(hotel_name)
    assert hotel_name in hotel_link


@allure.id("API-4")
@allure.title("Получение всей информации об отеле")
@allure.description("Корретное отображение отеля в базе")
def test_get_more_data():
    with allure.step("Указание интересующего отеля по его id"):
        hotel_name = 'moon2_hotel'
    with allure.step("Получение полной информации об отеле"):
        hotel_info = api.full_info_about_hotel(hotel_name)
    assert hotel_info["data"]["hotel"]["otahotel_id"] == hotel_name
    assert hotel_info["data"]["hotel"]["master_id"] > 0


@allure.id("API-5")
@allure.title("Поиск отелей в указанном регионе на определённую дату")
def test_search_for_data():
    with allure.step("Указание даты и региона для поиска отеля"):
        arrival = "2024-10-10"
        departure = "2024-10-17"
        region = 5580
    with allure.step("Получение информации о доступных вариантах"):
        hotels = api.search_for_data(arrival, departure, region)
    assert hotels["session_info"]["region_related"]["region"]["region_id"] == region
    assert hotels["total_hotels"] > 0
