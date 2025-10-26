from base.base_page import BasePage
from config.links import Links
from base.base_components.sidebar import Sidebar

class ProjectPage(BasePage):
    _PAGE_URL = Links.PROJECTS_PAGE

    _PROJECTS_PAGE = "//h1[text()='Проекты']"

    def __init__(self, driver):
        super().__init__(driver)
        self.sidebar = Sidebar(driver)

    def is_page_opened(self):
        element = self.ui.find(self._PROJECTS_PAGE, "Страница не открыта", True)
        assert element.is_displayed()