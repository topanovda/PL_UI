import platform
import time
import allure
from faker import Faker
from selenium.webdriver import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from metaclasses.meta_locator import MetaLocator

faker = Faker("ru_RU")
class UIHelper(metaclass=MetaLocator):

    os_name = platform.system()
    CMD_CTRL = Keys.COMMAND if os_name == "darwin" else Keys.CONTROL

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 15, poll_frequency=1)
        self.actions = ActionChains(self.driver)
        self.faker = Faker("ru_RU")

    def find(self, locator: tuple, message: str = "", wait : bool = True) -> WebElement:
        """
        Это метод для поиска элементов с использованием ожиданий
        :param locator: кортеж (используемый в метаклассах)
        :param message: сообщение об ошибке, если элемент не найден
        :param wait: использование ожиданий или просто поиск элемента
        :return: WebElement
        """
        if wait:
            element = self.wait.until(EC.visibility_of_element_located(locator), message=message)
        else:
            element = self.driver.find_element(*locator)
        return element

    def find_all(self, locator: tuple, message:str = "", wait: bool = True) -> list[WebElement]:
        """
        Метод для поиска всех элементов на странице
        :param locator: кортеж (используемый в метаклассах)
        :param message: сообщение об ошибке, если элемент не найден
        :param wait: использование ожиданий или просто поиск элемента
        :return: WebElement
        """
        if wait:
            element = self.wait.until(EC.visibility_of_all_elements_located(locator), message=message)
        else:
            element = self.driver.find_elements(*locator)
        return element

    def fill(self, locator: tuple, text: str):
        """
        Метод для заполнения полей
        :param locator: кортеж (используемый в метаклассах)
        :param text: текст который необходимо ввести в поле
        """
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator: tuple, message: str = ""):
        """
        Метод для клика по объекту
        :param locator: кортеж (используемый в метаклассах)
        :param message: сообщение об ошибке, если элемент не найден
        """
        self.wait.until(EC.element_to_be_clickable(locator), message=message).click()

    def screenshot(self, name: str = faker.name()):
        """
        Метод для прикрипления скриншотов в allure
        :param name: название файла генерируется через faker
        """
        allure.attach(
            body = self.driver.get_screenshot_as_png(),
            name = name,
            attachment_type = allure.attachment_type.PNG
        )

    def wait_for_invisibility(self, locator : WebElement, message : str = ""):
        """
        Метод ожидающий пропадания элемента на странице
        :param locator: кортеж (используемый в метаклассах)
        :param message: сообщение об ошибке, если элемент не найден
        """
        self.wait.until(EC.invisibility_of_element_located(locator), message=message)

    def wait_for_visibility(self, locator : WebElement, message : str = ""):
        """
        Метод ожидающий пропадания элемента на странице
        :param locator: кортеж (используемый в метаклассах)
        :param message: сообщение об ошибке, если элемент не найден
        """
        self.wait.until(EC.visibility_of_element_located(locator), message=message)

    def scroll_by(self, x, y):
        """
        Метод скролла на заданные координаты
        :param x: координаты по оси х
        :param y: координаты по оси y
        """
        self.driver.execute_script(f"window.scrollTo({x}, {y})")

    def scroll_to_bottom(self):
        """
        Метод скролла к низу сайта (в подвал)
        """
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_top(self):
        """
        Метод скрола вверх сайта
        """
        self.driver.execute_script("window.scrollTo(0, 0)")

    def scroll_to_element(self, locator):
        """
        Метод скролла к заданному элементы + 500 пикселей
        :param locator: кортеж (используемый в метаклассах)
        """
        self.actions.scroll_to_element(self.find(locator))
        self.driver.execute_script("""
        window.scrollTo({
            top: window.scrollY + 500,
        });
        """)