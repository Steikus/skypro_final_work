from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class MainPage:
    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.__driver.get("https://ostrovok.ru/")

    def register(self, mail_adress: str):
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class^='Control-module__control']")))
        self.__driver.find_element(By.CSS_SELECTOR, "div[class^='Control-module__control']").click()
        self.__driver.find_element(By.CSS_SELECTOR, "span[data-testid='user-widget-sign-up-tab']").click()
        self.__driver.find_element(By.CSS_SELECTOR, "input[data-testid='user-widget-sign-up-email-input']").send_keys(mail_adress)
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid='user-widget-sign-up-button']").click()
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class^='Control-module__username']")))
        username = self.__driver.find_element(By.CSS_SELECTOR, "div[class^='Control-module__username']").text
        return username

    def login(self, mail: str, password: str):
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class^='Control-module__control']")))
        self.__driver.find_element(By.CSS_SELECTOR, "div[class^='Control-module__control']").click()
        self.__driver.find_element(By.CSS_SELECTOR, "input[data-testid='user-widget-sign-in-email-input']").send_keys(mail)
        self.__driver.find_element(By.CSS_SELECTOR, "input[data-testid='user-widget-sign-in-password-input']").send_keys(password)
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid='user-widget-sign-in-button']").click()

    def get_login_from_orders(self):
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class^='Control-module__username']")))
        self.__driver.find_element(By.CSS_SELECTOR, "div[class^='Control-module__username']").click()
        self.__driver.find_element(By.CSS_SELECTOR, "a[data-testid='orders-link']").click()
        login = self.__driver.find_element(By.CSS_SELECTOR, "div.accountmenu-profile-email").text
        return login

    def searching_for_hotel(self, city: str, date_start: str, date_end: str):
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-testid='destination-input']")))
        self.__driver.find_element(By.CSS_SELECTOR, "input[data-testid='destination-input']").clear()
        self.__driver.find_element(By.CSS_SELECTOR, "input[data-testid='destination-input']").send_keys(city)
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class^='Suggest-module__hotel']")))
        self.__driver.find_element(By.CSS_SELECTOR, "input[data-testid='destination-input']").send_keys(Keys.RETURN)
        self.__driver.find_element(By.CSS_SELECTOR, "div[data-testid='date-start-input']").click()
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class^='Day-module__inner']")))
        actions = ActionChains(self.__driver)
        start_selector = self.__driver.find_element(By.CSS_SELECTOR, f"div[data-day*='{date_start}']")
        actions.move_to_element(start_selector).click().perform()
        end_selector = self.__driver.find_element(By.CSS_SELECTOR, f"div[data-day*='{date_end}']")
        actions.move_to_element(end_selector).click().perform()
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid='search-button']").click()

    def search_results_city(self):
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.zenregioninfo")))
        region_info = self.__driver.find_element(By.CSS_SELECTOR, "div.zenregioninfo").text
        return region_info

    def get_to_hotel_by_title(self, num: int):
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.zen-hotelcard-name-link.link")))
        hotels = self.__driver.find_elements(By.CSS_SELECTOR, "a.zen-hotelcard-name-link.link")
        original_window = self.__driver.current_window_handle
        hotels[num].click()
        WebDriverWait(self.__driver, 10).until(EC.number_of_windows_to_be(2))
        new_window = [window for window in self.__driver.window_handles if window != original_window][0]
        self.__driver.switch_to.window(new_window)

    def get_to_hotel_by_button(self, num: int):
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.zen-hotelcard-name-link.link")))
        hotels = self.__driver.find_elements(By.CSS_SELECTOR, "a[class^='zen-hotelcard-nextstep-button']")
        original_window = self.__driver.current_window_handle
        hotels[num].click()
        WebDriverWait(self.__driver, 10).until(EC.number_of_windows_to_be(2))
        new_window = [window for window in self.__driver.window_handles if window != original_window][0]
        self.__driver.switch_to.window(new_window)

    def get_hotel_name(self):
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.zen-roomspage-header-content")))
        name = self.__driver.find_element(By.CSS_SELECTOR, "h1.zen-roomspage-title-name")
        return name.text

    def add_to_favorite_page(self):
        self.__driver.find_element(By.CSS_SELECTOR, "div.link.zen-roomspage-header-icons-favorite").click()

    def go_to_favorite(self):
        self.__driver.get("https://ostrovok.ru/sp/favorite/")

    def get_favorite_hotel_name(self):
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href^='/rooms/']")))
        hotel_name = self.__driver.find_element(By.CSS_SELECTOR, "a[href^='/rooms/']").text
        return hotel_name

    def go_to_fav_from_title(self):
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-testid='destination-input']")))
        self.__driver.find_element(By.CSS_SELECTOR, "div[class^=FavoritesWidget-module__control]").click()
        original_window = self.__driver.current_window_handle
        WebDriverWait(self.__driver, 10).until(EC.number_of_windows_to_be(2))
        new_window = [window for window in self.__driver.window_handles if window != original_window][0]
        self.__driver.switch_to.window(new_window)
        header = self.__driver.find_element(By.CSS_SELECTOR, "div.zenfavorite-header").text
        return header

    def get_price_go_check(self, num: int):
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.zenroomspage-b2c-rates-deal")))
        prices = self.__driver.find_elements(By.CSS_SELECTOR, "div.zenroomspage-b2c-rates-price-amount")
        book_buttons = self.__driver.find_elements(By.CSS_SELECTOR, "a[class^='zenroomspage-b2c-rates-book']")
        price_to_check = prices[num].text
        book_buttons[num].click()
        return price_to_check

    def reserve_page_get_price(self):
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.zen-booking-bill-total-price-value")))
        price = self.__driver.find_element(By.CSS_SELECTOR, "div.zen-booking-bill-total-price-value").text
        return price
