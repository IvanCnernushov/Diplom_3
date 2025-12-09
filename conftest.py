import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from data.urls import URLs
from data.user import UserData
from locators.locators import LoginPageLocators
from pages.login_page import LoginPage

def create_driver(browser: str):

    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1366")
        options.add_argument("--height=768")

        return webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--remote-allow-origins=*")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    return webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to use: chrome or firefox"
    )

@pytest.fixture
def browser_choice(request):
    return request.config.getoption("--browser").lower()

@pytest.fixture
def driver(browser_choice):
    drv = create_driver(browser_choice)
    drv.delete_all_cookies()
    drv.implicitly_wait(5)

    yield drv
    drv.quit()

@pytest.fixture
def authorized_driver(driver):
    login = LoginPage(driver)
    login.open_page(URLs.LOGIN)
    login.wait_until_overlay_disappears()
    login.login(UserData.EMAIL, UserData.PASSWORD)
    login.wait_until_overlay_disappears()
    return driver