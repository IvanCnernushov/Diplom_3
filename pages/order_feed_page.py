import allure
from pages.base_page import BasePage
from locators.locators import MainPageLocators,OrderFeedPageLocators

class OrderFeedPage(BasePage):

    @allure.step("Получить количество выполнено за всё время")
    def get_total_counter(self):
            self.find_elements_with_wait(OrderFeedPageLocators.TOTAL_COUNTER)
            return self.find_element_with_wait(OrderFeedPageLocators.TOTAL_COUNTER).text

    @allure.step("Получить количество выполнено за сегодня")
    def get_today_counter(self):
            self.find_elements_with_wait(OrderFeedPageLocators.TODAY_COUNTER)
            return self.find_element_with_wait(OrderFeedPageLocators.TODAY_COUNTER).text
          
    @allure.step("Получить номер заказа, присвоенный при оформлении")
    def get_number_order(self):
        number_el = self.find_element_with_wait(OrderFeedPageLocators.NUMBER_ORDER)
        return int(number_el.text.strip())


    @allure.step("Получить номер заказа в разделе 'В работе'")
    def get_number_order_in_progress(self):
        elements = self.find_elements_with_wait(OrderFeedPageLocators.IN_PROGRESS_ORDERS)
        numbers = []
        for el in elements:
            txt = el.text.strip()
            if txt.isdigit():
                numbers.append(int(txt))
        return numbers
    
    @allure.step("Закрыть окно номера заказа")
    def close_window_number_order(self):
          self.wait_element_to_be_clickable(OrderFeedPageLocators.BUTTON_CLOSE_ORDER_NUMBER)
          self.click_to_element(OrderFeedPageLocators.BUTTON_CLOSE_ORDER_NUMBER)