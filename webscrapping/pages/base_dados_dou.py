# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from .base_page import BasePage


class BaseDados(BasePage):
    """
    Get access to DOU download-data page and downloads an given month.
    """
    YEAR_FIELD = (By.ID, 'ano-dados')
    MONTH_FIELD = (By.ID, 'mes-dados')
    LINK = (By.XPATH, '//li/a[contains(text(),"S03")]/@href')

    def _init__(self, driver):
        super().__init__(driver)

    def download(self, year, month):
        self.click_element(self.YEAR_FIELD, year)
        self.click_element(self.MONTH_FIELD, month)
        self.click_element(self.LINK)
