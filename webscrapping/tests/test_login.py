from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from basedriver import BaseDriver


def test_login():
    driver = BaseDriver().get_driver()
    login_page = LoginPage(driver)

    driver.get("http://127.0.0.1/login")
    login_page.login("username", "password")

    assert "dashboard" in driver.current_url

    driver.quit()

if __name__ == "__main__":
    test_login()
