import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from metaclasses.meta_locator import MetaLocator
from helpers.ui_helper import UIHelper
from pages.nsi_page.components.nsi_table_handler import NsiTableHandler
from data_builders.attribute_catalog_builder import AttributeCatalogBuilder


class BasePage(metaclass=MetaLocator):

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 10, 1)
        self.ui = UIHelper(self.driver)
        self.nsi_table = NsiTableHandler(self.driver)
        self.nsi_attribute_builder = AttributeCatalogBuilder()


    @allure.step("Открытие страницы")
    def open(self):
        with allure.step(f"Open {self._PAGE_URL} page"):
            self.driver.get(self._PAGE_URL)

    @allure.step("Проверка открытия страницы")
    def is_opened(self):
        self.wait.until(EC.url_to_be(self._PAGE_URL))

