# -*- coding: utf-8 -*-
"""
File: login_page.py
Location: webscrapping/pages
Created at: 30/10/2024
Author: Anderson Alves Monteiro <https://www.github.com/tekoryu>

Enter description here.
"""

from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME_FIELD  = (By.ID, 'username')