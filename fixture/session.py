
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login_by_cred(self, user):
        wd = self.app.wd
        self.app.navigation.open_login_form_from_header()
        wd.switch_to.frame("login_frame")
        self.fill_input_field_by_id('emailloginform-email', user.email)
        self.fill_input_field_by_id('emailloginform-password', user.password)
        wd.find_element_by_xpath('//button[@type="submit"]').click()
        wd.switch_to.default_content()

    def logout(self):
        wd = self.app.wd
        self.app.navigation.open_cabinet_page()
        wd.find_element_by_xpath('//span[contains(text(),"Вихід")]').click()

    def registration(self, user):
        wd = self.app.wd
        self.app.navigation.open_registration_page()
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
