from selenium import webdriver
from selenium.webdriver.common.by import By

from fixture.session import SessionHelper
from fixture.navigation import NavigationHelper



class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.navigation = NavigationHelper(self)

    def open_home_page(self, domain='https://rozetka.com.ua/'):
        wd = self.wd
        wd.get(domain)

    def open_login_form(self):
        wd = self.wd
        self.open_home_page()
        wd.find_element(By.XPATH, '//li[@class="header-actions__item header-actions__item--user"]').click()


    def open_registration_page(self):
        wd = self.wd
        self.open_login_form()
        wd.find_element(By.XPATH, '//button[@class="auth-modal__register-link button button--link ng-star-inserted"]').click()

    def destroy(self):
        self.wd.quit()
