import allure
import pickle
import os
from base.base_page import BasePage
from config.links import Links
from config.credentials import Credentials

@allure.epic("Login")
@allure.feature("Login")
class LoginPage(BasePage):

    _PAGE_URL = Links.HOST

    _EMAIL_FIELD = "//input[@id='email']"
    _PASSWORD_FIELD = "//input[@id='password']"
    _SUBMIT_BUTTON = "//button[@type='submit']"
    _UPDATE_BUTTON = "//div[@class='ant-modal-content']//button[@type='button']"

    @allure.step("Login as role: {role}")
    def login_as(self, role):
        allure.dynamic.label("role", role)  # добавляем роль как кастомный label
        if role == "admin": # Тут перечисляем нужные роли и имена файлов для их куков
            cookies_file = "cookies/admin-coolies.pkl"
        elif role == "user":
            cookies_file = "cookies/user-cookies.pkl"
        else:
            cookies_file = "cookies/cookies.pkl"

        if os.path.exists(cookies_file):
            # Подгружаем куки в браузер
            self.driver.delete_all_cookies()
            with open(cookies_file, "rb") as cookies_file:
                cookies = pickle.load(cookies_file)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
            self.driver.refresh()
        else:
            # Если файла с куки не существует, выполняет логин
            self.ui.fill(self._EMAIL_FIELD, Credentials.LOGIN)
            self.ui.fill(self._PASSWORD_FIELD, Credentials.PASSWORD)
            self.ui.click(self._SUBMIT_BUTTON, "Кнопка войти не найдена на странице")
            self.ui.click(self._UPDATE_BUTTON, "Кнопка обновить данные не найдена на странице")
            self.ui.wait_for_invisibility(self._UPDATE_BUTTON, "Кнопка не пропала со страницы")

    @allure.step("Login")
    def login(self):
        self.ui.fill(self._EMAIL_FIELD, Credentials.LOGIN)
        self.ui.fill(self._PASSWORD_FIELD, Credentials.PASSWORD)
        self.ui.click(self._SUBMIT_BUTTON, "Кнопка войти не найдена на странице")
        self.ui.click(self._UPDATE_BUTTON, "Кнопка обновить данные не найдена на странице")
        self.ui.wait_for_invisibility(self._UPDATE_BUTTON, "Кнопка не пропала со страницы")

