import allure
from pages.base_page import BasePage
from locators.locators import MainPageLocators
from data.urls import URLs
class MainPage(BasePage):

    @allure.step("Ждем невидимости оверлея")
    def wait_until_overlay_disappears(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)
  

    @allure.step("Кликнуть на ингредиент (используем INGREDIENT)")
    def click_on_ingredient(self):
        self.wait_element_to_be_clickable(MainPageLocators.INGREDIENT)
        self.click_to_element(MainPageLocators.INGREDIENT)

    @allure.step("Закрыть всплывающее окно")
    def close_window_details_ingredient(self):
        self.wait_element_to_be_clickable(MainPageLocators.WINDOW_DETAILS_INGREDIENT)
        self.click_to_element(MainPageLocators.CLOSING_WINDOW)

    @allure.step("Дождаться пока окно с деталями ингредиента станет невидимым")
    def wait_for_window_details_hide(self):
        return self.wait_for_element_hide(MainPageLocators.WINDOW_DETAILS_INGREDIENT)

    @allure.step("Перетащить элемент в корзину")
    def put_ingredient_into_basket(self):
        self.wait_until_overlay_disappears()
        ingredient = self.find_element_with_wait(MainPageLocators.INGREDIENT)
        basket = self.find_element_with_wait(MainPageLocators.BASKET)
        self.drag_and_drop_element(source=ingredient, target=basket)

    @allure.step("Получить значение счётчика ингредиента")
    def get_ingredient_counter(self):
        elements = self.driver.find_elements(*MainPageLocators.INGREDIENT_COUNTER)
        if not elements:
           return 0
        text = elements[0].text.strip()
        if not text.isdigit():
           return 
        return int(text)   

    @allure.step("Перейти в Конструктор")
    def go_to_constructor(self):
        self.wait_element_to_be_clickable(MainPageLocators.CONSTRUCTOR_NAV_BUTTON)
        self.click_to_element(MainPageLocators.CONSTRUCTOR_NAV_BUTTON)

    @allure.step("Открыть Ленту заказов")
    def go_to_order_feed(self):
        self.open_page(URLs.FEED)

    @allure.step("Кликнуть на Лента заказов")
    def click_on_order_feed(self):
        self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)

    