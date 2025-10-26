import time

from base.base_page import BasePage
from config.links import Links
from base.base_components.sidebar import Sidebar


class AttributePage(BasePage):
    _PAGE_URL = Links.ATTRIBUTE_PAGE
    _ADD_NEW_ELEMENT_BUTTON = "//button[@data-testid='nsi-button-element-add']"
    _ADD_NEW_ELEMENT = "//ul/li[@data-testid='nsi-actions-element']"
    _ADD_NEW_GROUP = "//ul/li[normalize-space() = 'Добавить группу']"
    _BUTTON_CATALOG_SAVE = "//button[@data-testid='nsi-button-catalog-save']"

    _TITLE_FIELD = "//input[@data-testid='nsi-input-element-title']"
    _CODE_FIELD = "//input[@data-testid='nsi-input-element-code']"
    _DESCRIPTION_FIELD = "//textarea[@data-testid='nsi-textarea-element-description']"
    _TYPE_DROPDOWN = "//div[@data-testid='nsi-select-atribute-type']"
    _LINK_ITEM = "//span[@data-testid='nsi-actions-atribute-type-link']"
    _STRING_ITEM = "//span[@data-testid='nsi-actions-atribute-type-string']"
    _NUMBER_ITEM = "//span[@data-testid='nsi-actions-atribute-type-number']"
    _DATE_ITEM = "//span[@data-testid='nsi-actions-atribute-type-date']"
    _BOOLEAN_ITEM = "//span[@data-testid='nsi-actions-atribute-type-boolean']"
    _GROUP_DROPDOWN = "//input[@id='group_id']"