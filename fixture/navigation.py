from selenium.webdriver.common.by import By


class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self, domain='https://auto.ria.com/'):
        wd = self.app.wd
        wd.get(domain)

    def open_cabinet_page(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element(By.XPATH, '//a[@href="/uk/cabinet"]').click()

    def open_login_form_from_header(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element(By.XPATH, '//a[@href="/uk/login.html?from_url=/uk/cabinet/"]').click()

    def open_registration_page(self):
        wd = self.app.wd
        self.open_login_form_from_header()
        wd.find_element(By.XPATH, '//button[@class="auth-modal__register-link button button--link ng-star-inserted"]').click()

    def open_menu(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element(By.XPATH, '//button[@class="header__button ng-tns-c94-1"]').click()

    def open_notepad_page_from_cabinet(self):
        wd = self.app.wd
        self.open_cabinet_page()
        wd.find_element(By.XPATH, '//a[@href="/uk/notepad.html"]')

    def open_subscribe_page_from_cabinet(self):
        wd = self.app.wd
        self.open_cabinet_page()
        wd.find_element(By.XPATH, '//a[@href="/uk/cabinet/subscribe"]')

