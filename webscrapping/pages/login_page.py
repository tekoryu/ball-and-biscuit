# -*- coding: utf-8 -*-
"""
File: login_page.py
Location: webscrapping/pages
Created at: 30/10/2024
Author: Anderson Alves Monteiro <https://www.github.com/tekoryu>

This is an example of use of the classes created for webscrapping.
"""

from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, 'username')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login_button')

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.input_text(*self.USERNAME_FIELD, username)
        self.input_text(*self.PASSWORD_FIELD, password)
        self.click_element(*self.LOGIN_BUTTON)