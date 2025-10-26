import allure
from base.base_test import BaseTest
import time
import pytest


class TestLoginPage(BaseTest):

    @pytest.mark.login
    def test_login(self):
        self.login_page.open()
        self.login_page.login_as("admin")
        with allure.step("Проверка что страница открыта"):
            self.project_page.is_page_opened()