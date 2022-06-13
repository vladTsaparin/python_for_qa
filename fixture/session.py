
class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login_by_cred(self, user_email, user_pass):
        wd = self.app.wd
        self.app.open_login_page()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(user_email)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(user_pass)
        wd.find_element_by_xpath("//button[@type='submit']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_name("email").click()

    def registration(self, user):
        wd = self.app.wd
        self.app.open_registration_page()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(user.email)
        wd.find_element_by_name("emailConfirm").click()
        wd.find_element_by_name("emailConfirm").clear()
        wd.find_element_by_name("emailConfirm").send_keys(user.email)
        wd.find_element_by_name("firstName").click()
        wd.find_element_by_name("firstName").clear()
        wd.find_element_by_name("firstName").send_keys(user.first_name)
        wd.find_element_by_name("lastName").click()
        wd.find_element_by_name("lastName").clear()
        wd.find_element_by_name("lastName").send_keys(user.last_name)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(user.password)
        wd.find_element_by_name("acceptTermsAndConditions").click()
        wd.find_element_by_xpath("//button[@type='submit']").click()
