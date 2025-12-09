import allure
import pytest

from data.urls import URLs
from pages.main_page import MainPage
from locators.locators import MainPageLocators


@allure.epic("Основная функциональность")
class TestMain:
    @allure.title("Переход по клику на «Конструктор»")
    def test_go_to_constructor(self, driver):
        page = MainPage(driver)
        page.wait_until_overlay_disappears()
        page.open_page(URLs.FEED)
        page.go_to_constructor()
        assert "Конструктор"

    @allure.title("Переход по клику на раздел «Лента заказов»")
    def test_go_to_order_feed(self, driver):
        page = MainPage(driver)
        page.open_page(URLs.MAIN)
        page.wait_until_overlay_disappears()
        page.click_on_order_feed()
        assert "Лента"  

    @allure.title("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_open_ingredient_modal(self, driver):
        page = MainPage(driver)
        page.open_page(URLs.MAIN)
        page.wait_until_overlay_disappears()
        page.click_on_ingredient()
        modal = page.find_element_with_wait(MainPageLocators.WINDOW_DETAILS_INGREDIENT)
        assert modal.is_displayed()

    @allure.title("Проверка закрытия всплывающего окна кликом по крестику")
    def test_close_window_details(self, driver):
        page = MainPage(driver)
        page.open_page(URLs.MAIN)
        page.wait_until_overlay_disappears()
        page.click_on_ingredient()
        page.close_window_details_ingredient()
        page.wait_for_window_details_hide()
        assert True, "Окно не закрылось"

    @allure.title("При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается")
    def test_ingredient_counter_increases(self, driver):
        page = MainPage(driver)
        page.open_page(URLs.MAIN)
        page.wait_until_overlay_disappears()
        before = page.get_ingredient_counter()
        page.put_ingredient_into_basket()
        page.wait_until_overlay_disappears()
        after = page.get_ingredient_counter()
        assert after > before, f"Счётчик не увеличился: было {before}, стало {after}"