from pages.login_page.page import LoginPage
from base.base_components.sidebar import Sidebar
from pages.project_page.page import ProjectPage
from pages.nsi_page.components.nsi_table_handler import NsiTableHandler
from pages.nsi_page.page import NsiPage
from data_builders.attribute_catalog_builder import AttributeCatalogBuilder
from pages.nsi_page.components.atribute_page import AttributePage

class BaseTest:

    def setup_method(self):
        self.login_page = LoginPage(self.driver)
        self.sidebar = Sidebar(self.driver)
        self.project_page = ProjectPage(self.driver)
        self.nsi_page = NsiPage(self.driver)
        self.nsi_table = NsiTableHandler(self.driver)
        self.nsi_attribute_builder = AttributeCatalogBuilder()
        self.nsi_attribute = AttributePage(self.driver)


