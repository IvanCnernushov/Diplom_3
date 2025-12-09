import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    @allure.step("Открыть страницу")
    def open_page(self, URLs):
        self.driver.get(URLs)

    @allure.step("Найти элемент с ожиданием")
    def find_element_with_wait(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    @allure.step("Подождать видимости элемента")
    def find_elements_with_wait(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    @allure.step("Подождать пока элемент станет невидимым")
    def wait_for_element_hide(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Подождать кликабельности элемента")
    def wait_element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center', inline:'nearest'});", element
        )

    @allure.step("Кликнуть на элемент")
    def click_to_element(self, locator):
        element = self.wait_element_to_be_clickable(locator)
        self.scroll_to_element(locator)
        element.click()

    @allure.step("Перетащить элемент")
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)
    
    @allure.step("Подождать появления хотя бы одного элемента: {locator}")
    def wait_for_any_element(self, locator, timeout=None):
        wait_time = timeout if timeout else self.timeout
        return WebDriverWait(self.driver, wait_time).until(
        EC.presence_of_element_located(locator)
    )

    @allure.step("Ожидать исчезновения оверлея (модалки)")
    def wait_until_overlay_disappears(self):
        from locators.locators import MainPageLocators
        return self.wait_for_element_hide(MainPageLocators.OVERLAY)
    
