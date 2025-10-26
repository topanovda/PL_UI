import allure

from base.base_test import BaseTest
from data_builders.attribute_catalog_builder import AttributeCatalogBuilder
import time
import pytest

@allure.feature("Справочники")
class TestNSIPage(BaseTest):

    @pytest.mark.smoke
    @allure.feature("Переход в раздел Справочники")
    def test_open_nsi_page(self):
        self.login_page.open()
        self.login_page.login_as("admin")
        self.project_page.is_page_opened()
        self.sidebar.select_role("planer")
        self.nsi_page.open()
        self.nsi_page.is_page_opened()

    @pytest.mark.smoke
    @allure.feature("Переход в раздел справочников {catalog_name}")
    @pytest.mark.parametrize("action", ["open", "edit"])
    @pytest.mark.parametrize("catalog_name", ["Типы проектов", "Атрибуты", "Показатели", "Базовые календари", "Единицы измерения", "Типы версий", "Статусы версий"])
    def test_open_attributes(self, action, catalog_name):
        allure.dynamic.label("catalog_name", catalog_name)
        with allure.step("Открытие страницы"):
            self.login_page.open()
        with allure.step("Авторизация как admin"):
            self.login_page.login_as("admin")
        with allure.step("Проверка что страница открыта"):
            self.project_page.is_page_opened()
        with allure.step("Переход в под роль Планировщик"):
            self.sidebar.select_role("planer")
        with allure.step("Переход на страницу Справочники"):
            self.nsi_page.open()
        with allure.step("Проверка что страница открыта"):
            self.nsi_page.is_page_opened()
        with allure.step(f"Переход в каталог '{catalog_name}' с действием '{action}'"):
            self.nsi_page.open_catalog(catalog_name, action)

    @pytest.mark.smoke
    @allure.feature("переход к созданию элемента справочника")
    def test_open_create_element(self):
        # Считаем количество строк ДО

        attribute_data = (
            AttributeCatalogBuilder()
            .build()
        )
        with allure.step("Открытие страницы"):
            self.login_page.open()
        with allure.step("Авторизация как admin"):
            self.login_page.login_as("admin")
        with allure.step("Проверка что страница открыта"):
            self.project_page.is_page_opened()
        with allure.step("Переход в под роль Планировщик"):
            self.sidebar.select_role("planer")
        with allure.step("Переход на страницу Справочники"):
            self.nsi_page.open()
        with allure.step("Проверка что страница открыта"):
            self.nsi_page.is_page_opened()
        with allure.step("Переход в каталог 'Атрибуты'"):
            self.nsi_page.open_catalog("Атрибуты", "open")
            old_count = self.nsi_table.row_count
            print(old_count)
        self.nsi_page.open_create_element()
        with allure.step("Заполняем форму атрибута"):
            self.nsi_page.fill_form(attribute_data)
            # Проверка увеличения строк
            self.nsi_table.wait_for_new_row(old_count)
        #     # Проверяем, что запись появилась
        # self.nsi_table.assert_row_added(attribute_data["title"])

