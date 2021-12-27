# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_app_dynamics_job(self):
        wd = self.wd
        wd.get("https://netfanz:1qaz2wsx0@netfanz.inprogress.rocks/auth/login")
        self.login(wd, user_email="influencer_1634565141@netfanz.com", user_pass="influencer_1634565141")

    def login(self, wd, user_email, user_pass):
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(user_email)
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(user_pass)
        wd.find_element_by_xpath("//button[@type='submit']").click()
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
