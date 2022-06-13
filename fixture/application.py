from selenium import webdriver
from selenium.webdriver.common.by import By

from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def open_home_page(self, domain):
        wd = self.wd
        wd.get(domain)
        self.cookies_accept()

    def open_login_page(self):
        wd = self.wd
        self.open_home_page('https://jysk.ua/')
        wd.find_element(By.XPATH, '//a[@href="/customer/login"]').click()

    def cookies_accept(self):
        wd = self.wd
        wd.find_element(By.CLASS_NAME, 'coi-banner__accept').click()

    def open_registration_page(self):
        wd = self.wd
        self.open_login_page()
        wd.find_element(By.XPATH, '//a[@href="/customer/create"]').click()

    def destroy(self):
        self.wd.quit()
