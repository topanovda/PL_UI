import time

from selenium.webdriver.chrome.webdriver import WebDriver
from faker import Faker
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from metaclasses.meta_locator import MetaLocator



class NsiTableHandler(metaclass=MetaLocator):
    _SYSTEM_TABLE_LOCATOR = "(//div[contains(@class, 'ant-table-wrapper')])[1]"
    _ROWS_LOCATOR = ".//tbody//tr"
    _CELLS_LOCATOR = ".//td"
    # _ATTRIB_LOCATOR_TEXT = "(.//td//span)[2]"
    _ATTRIB_LOCATOR_TEXT = ".//tr[.//td//span[contains(text(), 'Штаб низкий зарплата эпоха поздравлять. Бетонный армейский поставить строительство четко.')]]"
    _EDIT_BUTTON = ".//button[@data-testid='nsi-button-catalog-edit']"
    _OPEN_BUTTON = ".//button[@data-testid='nsi-button-catalog-open']"
    _CUSTOMER_TABLE_LOCATOR = "(//div[contains(@class, 'ant-table-wrapper')])[2]"

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 15, poll_frequency=1)
        self.actions = ActionChains(self.driver)
        self.faker = Faker("ru_RU")

    @property
    def _table(self) -> WebElement:
        return self.driver.find_element(*self._SYSTEM_TABLE_LOCATOR)

    @property
    def _rows(self) -> list[WebElement]:
        table = self._table
        return table.find_elements(*self._ROWS_LOCATOR)

    @property
    def row_count(self) -> int:
        return len(self._rows)
    #
    # def get_cell_content(self, row_number, column_number):
    #     row = self._rows[row_number - 1]
    #     cell = row.find_elements(*self._CELLS_LOCATOR)[column_number - 1]
    #     return cell.text
    #
    # def get_row_content(self, row_number):
    #     row = self._rows[row_number - 1]
    #     return [cell.text for cell in row.find_elements(*self._CELLS_LOCATOR)]
    #
    # def get_column_content(self, column_number):
    #     column_content = []
    #     for row in self._rows:
    #         cells = row.find_elements(*self._CELLS_LOCATOR)
    #         column_content.append(cells[column_number - 1].text)
    #     return column_content
    #
    # def select_row(self, row_number):
    #     row = self._rows[row_number - 1]
    #     cell = row.find_elements(*self._CELLS_LOCATOR)[0]
    #     cell.click()

    def select_row_by_text(self, catalog_name: str, action: str):
        """
        Ищет строку по названию каталога и выполняет действие open | edit
        :param catalog_name: Название каталога
        :param action: Действие open или edit
        :return:
        """
        for row in self._rows:
            # Получаем все ячейки в строке
            cells = row.find_elements(*self._CELLS_LOCATOR)

            # Проверяем, содержится ли нужный текст хотя бы в одной ячейке
            if any(catalog_name in cell.text for cell in cells):
                if action == "edit":
                    row.find_element(*self._EDIT_BUTTON).click()
                    return
                elif action == "open":
                    row.find_element(*self._OPEN_BUTTON).click()
                    return
                else:
                    raise AssertionError("Неверное значение параметра action")

        # Если цикл завершился без return, значит совпадение не найдено
        raise ValueError(f"Строка с названием '{catalog_name}' не найдена")


    def find_row_by_text(self):
        """
        , name: str, action: str
        Ищет строку по названию и выполняет действие open | edit | text
        :param name: Название
        :param action: Действие open, edit, text
        :return:
        """

        for row in self._rows:
            # Получаем все ячейки в строке
            cells = row.find_elements(*self._ATTRIB_LOCATOR_TEXT)
            print(cells)

            # # Проверяем, содержится ли нужный текст хотя бы в одной ячейке
            # if any(name in cell.text for cell in cells):
            #     if action == "edit":
            #         row.find_element(*self._EDIT_BUTTON).click()
            #         return
            #     elif action == "open":
            #         row.find_element(*self._OPEN_BUTTON).click()
            #         return
            #     elif action == "text":
            #
            #         return row.text
            #     else:
            #         raise AssertionError("Неверное значение параметра action")

        # Если цикл завершился без return, значит совпадение не найдено
        # raise ValueError(f"Строка с названием '{name}' не найдена")

    def wait_for_new_row(self, old_count: int, timeout: int = 10):
        """
        Ждём появления новой строки в таблице.
        :param old_count: количество строк ДО добавления
        :param timeout: время ожидания (сек)
        """
        WebDriverWait(self.driver, timeout).until(
            lambda driver: self.row_count > old_count,
            message=f"Количество строк не увеличилось (старое значение: {old_count}, текущее: {self.row_count})"
        )

    def assert_row_added(self, title: str):
        """
        Проверяет, что строка с переданным title появилась в таблице
        """
        locator = (f".//span[contains(normalize-space(.), '{title}')]]")
        row = self.wait.until(EC.visibility_of_element_located(locator),
            message=f"Строка с названием '{title}' не появилась в таблице")
        assert title in row.text, f"В строке нет ожидаемого текста: {title}"

