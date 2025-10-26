import random
from faker import Faker
import allure

faker = Faker("ru_RU")

class AttributeCatalogBuilder:
    def __init__(self):
        self._data = {
            "title": faker.text(max_nb_chars=100),
            "type": random.choice(["link", "string", "number", "date", "boolean"]),
            "code": faker.text(max_nb_chars=100),
            "description": faker.text(max_nb_chars=500)
        }

    @allure.step("Установить title")
    def with_title(self, title: str):
        """Установить своё значение title"""
        self._data["title"] = title
        allure.dynamic.parameter("Title", title)
        return self

    @allure.step("Установить тип атрибута")
    def with_type(self, attr_type: str):
        """Установить свой тип"""
        if attr_type not in ["link", "string", "number", "date", "boolean"]:
            raise ValueError(f"Недопустимый тип: {attr_type}")
        self._data["type"] = attr_type
        allure.dynamic.parameter("Type", attr_type)
        return self

    @allure.step("Установить код")
    def with_code(self, code: str):
        """Установить свой код"""
        self._data["code"] = code
        allure.dynamic.parameter("Code", code)
        return self

    @allure.step("Установить описание")
    def with_description(self, description: str):
        """Установить своё описание"""
        self._data["description"] = description
        allure.dynamic.parameter("Description", description)
        return self

    @allure.step("Собрать атрибут")
    def build(self):
        """Получить готовый словарь"""
        # Прикрепляем финальные данные к шагу в виде JSON
        allure.attach(str(self._data), name="Final Attribute Data", attachment_type=allure.attachment_type.JSON)
        return self._data
