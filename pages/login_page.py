import allure
from pages.base_page import BasePage
from locators.locators import LoginPageLocators


class LoginPage(BasePage):

    @allure.step("Авторизация пользователя")
    def login(self, email: str, password: str):
        self.find_element_with_wait(LoginPageLocators.EMAIL_FIELD).send_keys(email)
        self.find_element_with_wait(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.click_to_element(LoginPageLocators.LOGIN_BUTTON)
