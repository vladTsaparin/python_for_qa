from selenium import webdriver

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)

    def open_login_page(self):
        wd = self.wd
        wd.get("https://netfanz:1qaz2wsx0@netfanz.inprogress.rocks/auth/login")

    def login_by_cred(self, user_email, user_pass):
        wd = self.wd
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(user_email)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(user_pass)
        wd.find_element_by_xpath("//button[@type='submit']").click()


    def destroy (self):
        self.wd.quit()
