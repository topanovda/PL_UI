import allure

from base.base_test import BaseTest
import time
import pytest


class TestProjectPage(BaseTest):

    @pytest.mark.smoke
    @allure.feature("Смена подроли пользователя")
    def test_switch_role(self):
        self.login_page.open()
        self.login_page.login_as("admin")
        self.project_page.is_page_opened()
        self.sidebar.select_role("planer")
        self.project_page.is_page_opened()