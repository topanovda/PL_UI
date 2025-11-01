import os
import pytest
from selenium import webdriver

@pytest.fixture(scope="function", autouse=True)
def get_driver(request):
    if os.environ["BROWSER"] == "chrome":
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")  # Запускает браузер в режиме без графического интерфейса (удобно для серверов)
        options.add_argument("--no-sandbox")  # Отключает режим песочницы для предотвращения проблем с правами доступа
        options.add_argument("--disable-dev-shm-usage")  # Отключает использование общей памяти /dev/shm (для Docker и серверных сред)
        options.add_argument("--disable-gpu")  # Отключает GPU, необходимое для headless-режима на некоторых системах
        options.add_argument("--window-size=1920,1080")  # Устанавливает фиксированный размер окна браузера
        # options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
        request.cls.driver = driver
        yield driver
        driver.quit()


    elif os.environ["BROWSER"] == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
        request.cls.driver = driver
        yield driver
        driver.quit()