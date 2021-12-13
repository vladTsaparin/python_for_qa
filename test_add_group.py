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
        wd.get("https://www.katalon.com/sign-in/")
        self.login(wd, user_email="vlad.caparin51+katalon@gmail.com", user_pass="3W3L5Mn8cJh4pqK!")

    def login(self, wd, user_email, user_pass):
        wd.find_element_by_name("user_email").click()
        wd.find_element_by_name("user_email").clear()
        wd.find_element_by_name("user_email").send_keys(user_email)
        wd.find_element_by_name("user_pass").click()
        wd.find_element_by_name("user_pass").clear()
        wd.find_element_by_name("user_pass").send_keys(user_pass)
        wd.find_element_by_xpath("//input[@type='submit']").click()
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
