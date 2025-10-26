import time

import allure

from base.base_page import BasePage
from config.links import Links
from base.base_components.sidebar import Sidebar
from pages.nsi_page.components.atribute_page import AttributePage

@allure.epic("Справочники")
@allure.feature("Спровочники")
class NsiPage(BasePage):
    _PAGE_URL = Links.NSI_PAGE
    _NSI_PAGE = "//h1[text()='Нормативно-справочная информация']"

    _BUTTON_CATALOG_SAVE = "//button[@data-testid='nsi-button-catalog-save']"
    _BUTTON_ELEMENT_SAVE = "//button[@data-testid='nsi-button-element-save']"
    _SEARCH_FIELD = "//input[@data-testid='nsi-input-catalog-search']"
    _SEARCH_BUTTON = "//span[@class='ant-input-group-addon']"
    _ADD_CUSTOMER_CATALOG_BUTTON = "//button[@data-testid='nsi-button-catalog-add']"



    def __init__(self, driver):
        super().__init__(driver)
        self.sidebar = Sidebar(driver)
        self.nsi_attribute = AttributePage(driver)

    @allure.step("Проверка открыта ли страница")
    def is_page_opened(self):
        element = self.ui.find(self._NSI_PAGE, "Страница не открыта", True)
        assert element.is_displayed()

    @allure.step("Переход в каталог: {catalog_name}")
    def open_catalog(self, catalog_name: str, action: str):
        """
        Ищет строку по названию каталога и выполняет действие open | edit
        :param catalog_name: Название каталога
        :param action: Действие open или edit
        :return:
        """
        allure.dynamic.label("catalog_name", catalog_name)  # добавляем роль как кастомный label
        self.nsi_table.select_row_by_text(catalog_name, action)
        header_locator = ("xpath", f"//h1[normalize-space(text())='{catalog_name}']")
        if action == "open":
            assert self.ui.find(header_locator, f"Заголовок '{catalog_name}' не найден на странице", True)
        elif action == "edit":
            assert self.ui.find(self._BUTTON_CATALOG_SAVE, "Кнопка не найдена на странице", True)

    @allure.step("Переход к созданию элемента справочника")
    def open_create_element(self):
        self.ui.click(self.nsi_attribute._ADD_NEW_ELEMENT_BUTTON, f"Кнопка не найдена на странице")
        self.ui.click(self.nsi_attribute._ADD_NEW_ELEMENT, f"Кнопка не найдена на странице")
        assert self.ui.find(self.nsi_attribute._BUTTON_CATALOG_SAVE, "Кнопка не найдена на странице", True)

    def fill_form(self, nsi_attribute_builder: dict):
        title = nsi_attribute_builder["title"]
        self.ui.fill(self.nsi_attribute._TITLE_FIELD, title)
        self.ui.fill(self.nsi_attribute._CODE_FIELD, nsi_attribute_builder["code"])
        self.ui.click(self.nsi_attribute._TYPE_DROPDOWN, "Выпадающий список типов элементов не найден")
        self.ui.click(self.nsi_attribute._STRING_ITEM, "Элемент списка не найден")
        self.ui.fill(self.nsi_attribute._DESCRIPTION_FIELD, nsi_attribute_builder["description"])
        self.ui.click(self.nsi_attribute._BUTTON_CATALOG_SAVE, "Кнопка 'Сохранить' не найдена на странице")

        # allure.dynamic.label("name", title)  # добавляем роль как кастомный label

        time.sleep(3)

    def find_row_by_text(self, name):
        assert self.nsi_table.find_row_by_text() == name
