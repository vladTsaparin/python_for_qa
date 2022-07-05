from selenium.webdriver.common.by import By


class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self, domain='https://auto.ria.com/'):
        wd = self.app.wd
        wd.get(domain)

    def open_login_form_from_header(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element(By.XPATH, '//span[@class="tl"]').click()

    def open_registration_page(self):
        wd = self.app.wd
        self.open_login_form_from_header()
        wd.find_element(By.XPATH,
                        '//button[@class="auth-modal__register-link button button--link ng-star-inserted"]').click()

    def open_personal_information_page_from_menu(self):
        wd = self.app.wd
        self.open_home_page()

        wd.find_element(By.XPATH, '//a[@href="https://rozetka.com.ua/cabinet/personal-information"]').click()

    def open_menu(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element(By.XPATH, '//button[@class="header__button ng-tns-c94-1"]').click()

    def open_wishlist_page_from_menu(self):
        wd = self.app.wd
        self.open_menu()
        wd.find_element(By.XPATH, '//a[@href="https://rozetka.com.ua/cabinet/wishlist/"]').click()
