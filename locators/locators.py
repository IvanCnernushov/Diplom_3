from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_NAV_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    FIRST_INGREDIENT = (By.XPATH, "(//img[@alt='Флюоресцентная булка R2-D3'])")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class,'Modal')]")
    CONSTRUCTOR_TOP = (By.XPATH, "//span[text()='Перетяните булочку сюда (верх)']")
    CONSTRUCTOR_BOTTOM = (By.XPATH, "//span[text()='Перетяните булочку сюда (низ)']")
    MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    INGREDIENT_COUNTER = (By.XPATH, "//div[contains(@class,'counter_counter')]/p")
    INGREDIENT_CARD = (By.XPATH, "(//div[contains(@class,'IngredientCard')])[1]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_NUMBER = (By.XPATH,"//h2[contains(@class,'Modal_modal__title') and contains(@class,'digits-large')]")
    OVERLAY = (By.XPATH,".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")
    WINDOW_DETAILS_INGREDIENT = (By.XPATH,"//div[contains(@class, 'Modal_modal__contentBox__sCy8X pt-10 pb-15')]")
    CLOSING_WINDOW = (By.XPATH,"//button[contains(@class, 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK')]")
    INGREDIENT = (By.XPATH,"//p[contains(@class, 'BurgerIngredient_ingredient__text__yp3dH')]")
    BASKET = (By.XPATH,"//ul[contains(@class, 'BurgerConstructor_basket__list__l9dp_')]")


class OrderFeedPageLocators:
    TODAY_COUNTER = (By.XPATH,"//p[contains(text(),'Выполнено за сегодня')]/following::p[contains(@class,'OrderFeed_number__')][1]")
    IN_PROGRESS_ORDERS = (By.XPATH,"//ul[contains(@class, 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi')]/li[contains(@class, 'text text_type_digits-default mb-2')]")
    TOTAL_COUNTER = (By.XPATH, "//p[contains(@class,'digits-large')]")
    NUMBER_ORDER = (By.XPATH,"//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8')]")
    BUTTON_CLOSE_ORDER_NUMBER = (By.XPATH,"//button[contains(@class, 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK')]") 

class LoginPageLocators:
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")