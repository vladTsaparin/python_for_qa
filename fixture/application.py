from selenium import webdriver
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def open_login_page(self):
        wd = self.wd
        wd.get("https://netfanz:2qaz2wsx0@netfanz.inprogress.rocks/auth/login")

    def destroy(self):
        self.wd.quit()
