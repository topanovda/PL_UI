from fixtures.ui_fixtures import *
import allure

def pytest_exception_interact(node, call, report):
    driver = node.instance.driver
    allure.attach(
        body=driver.get_screenshot_as_png(),  # Делает скриншот
        name="Ошибка",  # Дает имя скриншоту
        attachment_type=allure.attachment_type.PNG  # Крепит скриншот к отчету в формате .png
    )