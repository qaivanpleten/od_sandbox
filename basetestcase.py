import unittest
from selenium import webdriver

class BaseTestCase(unittest.TestCase):
    def setUp(self):

        # create new Chrome session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the home page
        self.driver.get("http://www.sandbox.opendrive.com/login")

    def tearDown(self):
        # close the browser window
        self.driver.quit()