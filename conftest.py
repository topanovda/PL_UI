from fixtures.ui_fixtures import *
import allure

# def pytest_exception_interact(node, call, report):
#     driver = node.instance.driver
#     allure.attach(
#         body=driver.get_screenshot_as_png(),  # Делает скриншот
#         name="Ошибка",  # Дает имя скриншоту
#         attachment_type=allure.attachment_type.PNG  # Крепит скриншот к отчету в формате .png
#     )


def pytest_exception_interact(node, call, report):
    """
    Делает скриншот браузера при падении теста, если driver существует.
    Безопасен для случаев, когда фикстура не была инициализирована.
    """
    # Проверяем, есть ли вообще тестовый инстанс
    instance = getattr(node, "instance", None)
    if not instance:
        return

    # Проверяем, есть ли у него driver
    driver = getattr(instance, "driver", None)
    if not driver:
        return

    # Пробуем сделать скриншот
    try:
        allure.attach(
            body=driver.get_screenshot_as_png(),
            name="Ошибка",
            attachment_type=allure.attachment_type.PNG
        )
    except Exception as e:
        print(f"[pytest_exception_interact] Не удалось сделать скриншот: {e}")
