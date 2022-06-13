from selenium import webdriver
from selenium.webdriver.common.by import By

from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def open_login_page(self):
        wd = self.wd
        wd.get("https://jysk.ua/customer/login")
        self.cookies_accept()

    def cookies_accept(self):
        wd = self.wd
        wd.find_element(By.CLASS_NAME, 'coi-banner__accept').click()

    def open_registration_page(self):
        wd = self.wd
        wd.get("https://jysk.ua/customer/create")
        self.cookies_accept()

    def destroy(self):
        self.wd.quit()
