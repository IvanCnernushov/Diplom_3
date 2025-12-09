import allure
import pytest

from data.urls import URLs
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from locators.locators import MainPageLocators,OrderFeedPageLocators


@allure.epic("Лента заказов")
class TestOrderFeed:
    @allure.title("При создании нового заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_total_counter_increases(self, authorized_driver):
        driver = authorized_driver
        feed = OrderFeedPage(driver)
        main = MainPage(driver)
        feed.open_page(URLs.FEED)
        before = feed.get_total_counter()
        main.open_page(URLs.MAIN)
        main.wait_until_overlay_disappears()
        main.put_ingredient_into_basket()
        main.click_to_element(MainPageLocators.PLACE_ORDER_BUTTON)
        feed.open_page(URLs.FEED)
        after = feed.get_total_counter()
        assert after >= before

    @allure.title("При создании нового заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_today_counter_increases(self, authorized_driver):
        driver = authorized_driver
        feed = OrderFeedPage(driver)
        main = MainPage(driver)
        feed.open_page(URLs.FEED)
        before = feed.get_today_counter()
        main.open_page(URLs.MAIN)
        main.wait_until_overlay_disappears()
        main.put_ingredient_into_basket()
        main.click_to_element(MainPageLocators.PLACE_ORDER_BUTTON)
        feed.open_page(URLs.FEED)
        after = feed.get_today_counter()
        assert after >= before

    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_number_order_in_progress(self, authorized_driver):
        driver = authorized_driver
        feed = OrderFeedPage(driver)
        main = MainPage(driver)
        main.open_page(URLs.MAIN)
        main.wait_until_overlay_disappears()
        main.put_ingredient_into_basket()
        main.click_to_element(MainPageLocators.PLACE_ORDER_BUTTON)
        main.wait_until_overlay_disappears()
        number_order = feed.get_number_order()
        main.click_to_element(OrderFeedPageLocators.BUTTON_CLOSE_ORDER_NUMBER)
        main.wait_until_overlay_disappears()
        main.go_to_order_feed()
        main.wait_until_overlay_disappears()
        in_progress_numbers = feed.get_number_order_in_progress()
        assert number_order in in_progress_numbers