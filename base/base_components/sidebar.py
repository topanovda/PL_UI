from base.base_page import BasePage
from config.links import Links
import allure

class Sidebar(BasePage):

    _PROJECT_PAGE = Links.PROJECTS_PAGE
    _ROLE_ITEMS = "//div[contains(@class, 'ant-dropdown-trigger')]"
    _PLANNER_ROLE = "//li[@role='menuitem']//span[text() = 'Планировщик']"
    _MANAGER_ROLE = "//li[@role='menuitem']//span[text() = 'Руководитель']"
    _EXECUTOR_ROLE = "//li[@role='menuitem']//span[text() = 'Исполнитель']"
    _TEAM_MANAGEMENT_ROLE = "//li[@role='menuitem']//span[text() = 'Управление командой']"
    _ADMIN_ROLE = "//li[@role='menuitem']//span[text() = 'Администратор']"

    def __init__(self, driver):
        super().__init__(driver)
        self._ROLES = {
            "planer": self._PLANNER_ROLE,
            "manager": self._MANAGER_ROLE,
            "executor": self._EXECUTOR_ROLE,
            "team_management": self._TEAM_MANAGEMENT_ROLE,
            "admin": self._ADMIN_ROLE
        }

    @allure.step("Выбор подроли представления меню")
    def select_role(self, role):
        if role not in self._ROLES:
            raise ValueError(f"Роль '{role}' не найдена в доступных ролях: {list(self._ROLES.keys())}")
        self.ui.click(self._ROLE_ITEMS)
        self.ui.click(self._ROLES[role])
