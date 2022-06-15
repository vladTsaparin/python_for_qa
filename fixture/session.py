
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login_by_cred(self, user):
        wd = self.app.wd
        self.app.open_login_form()
        self.fill_input_field_by_id('auth_email', user.email)
        self.fill_input_field_by_id('auth_pass', user.password)
        #wd.find_element_by_xpath('//label[@class="auth-modal__remember-checkbox"]').click()
        wd.find_element_by_xpath('//button[@class="button button--large button--green auth-modal__submit ng-star-inserted"]').click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_name("email").click()

    def registration(self, user):
        wd = self.app.wd
        self.app.open_registration_page()
        self.fill_input_field_by_id('registerUserName', user.first_name)
        self.fill_input_field_by_id('registerUserSurname', user.last_name)
        self.fill_input_field_by_id('registerUserPhone', user.phone)
        self.fill_input_field_by_id('registerUserEmail', user.email)
        self.fill_input_field_by_id('registerUserPassword', user.password)
        wd.find_element_by_xpath("//button[@class='button button--large button--green auth-modal__submit']").click()

    def fill_input_field_by_id(self, field_id, value):
        wd = self.app.wd
        wd.find_element_by_id(field_id).click()
        wd.find_element_by_id(field_id).clear()
        wd.find_element_by_id(field_id).send_keys(value)
