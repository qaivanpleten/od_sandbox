import unittest, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()                                  #can use Firefox or Chrome
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.title
        cls.driver.get("http://www.sandbox.opendrive.com/login")          #navigation to login page

    def test_1_forgot_password(self):
        self.driver.find_element_by_xpath('//body/div/div/div/div/form/div/div/span/a[@href="/forgot"]').click()
        assert "https://sandbox.opendrive.com/forgot" in self.driver.current_url
        self.driver.get("http://www.sandbox.opendrive.com/login")

    def test_2_invalid_username_and_pass(self):
        assert "MyDrive - Login" in self.driver.title
        username = self.driver.find_element_by_id("login_username")
        username.click()
        username.send_keys("invalid_username_and_pass")
        password = self.driver.find_element_by_id("login_password")
        password.click()
        password.send_keys("sfkjghsdlf")
        password.submit()
        assert "Invalid username or password" in self.driver.page_source

    def test_3_invalid_username(self):
        username = self.driver.find_element_by_id("login_username")
        username.click()
        username.send_keys("invalid@mail")
        password = self.driver.find_element_by_id("login_password")
        password.click()
        password.send_keys("rootpass")
        password.submit()
        assert "Invalid username or password" in self.driver.page_source

    def test_4_invalid_password(self):
        username = self.driver.find_element_by_id("login_username")
        username.click()
        username.send_keys("qa.ivanpleten@gmail.com")
        password = self.driver.find_element_by_id("login_password")
        password.click()
        password.send_keys("sfkjghsdjhgfjhgfjhgfjhgfjghfjhgfjhgfjhfgjhgfjhgflf")
        password.submit()
        assert "MyDrive - MyDrive" not in self.driver.page_source

    def test_5_valid_values(self):
        username = self.driver.find_element_by_id("login_username")
        username.click()
        username.send_keys("qa.ivanpleten@gmail.com")
        password = self.driver.find_element_by_id("login_password")
        password.click()
        password.send_keys("rootpass")
        password.submit()
        assert "MyDrive" in self.driver.page_source

        self.driver.delete_all_cookies()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == '__main__':
        unittest.main()

#qa pass