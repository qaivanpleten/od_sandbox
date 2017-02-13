import unittest, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from faker import Faker
f = Faker()

class registration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://www.sandbox.opendrive.com/signup")                  #Open page and wait
        cls.driver.title

    def test_1_empty_form(self):
        self.driver.get("http://www.sandbox.opendrive.com/signup")
        assert "OpenDrive – OpenDrive Sign Up" in self.driver.title
        self.driver.find_element_by_id("signup-submit-btn").click()
        assert "Oops" in self.driver.page_source

    def test_2_only_first_name(self):
        self.driver.get("http://www.sandbox.opendrive.com/signup")
        assert "OpenDrive – OpenDrive Sign Up" in self.driver.title
        first_name = self.driver.find_element_by_id("signup-first-name")
        first_name.click()
        first_name.send_keys("John")
        first_name.submit()
        assert "Oops" in self.driver.page_source

    def test_3_only_last_name(self):
        self.driver.get("http://www.sandbox.opendrive.com/signup")
        assert "OpenDrive – OpenDrive Sign Up" in self.driver.title
        last_name = self.driver.find_element_by_id("signup-last-name")
        last_name.click()
        last_name.send_keys("Doe")
        last_name.submit()
        assert "Oops" in self.driver.page_source

    def test_4_only_email(self):
        self.driver.get("http://www.sandbox.opendrive.com/signup")
        assert "OpenDrive – OpenDrive Sign Up" in self.driver.title
        email = self.driver.find_element_by_id("signup-email")
        email.click()
        email.send_keys("autotest@gmail.com")
        email.submit()
        assert "Oops" in self.driver.page_source

    def test_5_only_password(self):
        self.driver.get("http://www.sandbox.opendrive.com/signup")
        assert "OpenDrive – OpenDrive Sign Up" in self.driver.title
        password = self.driver.find_element_by_id("signup-password")
        password.click()
        password.send_keys("rootpass")
        password.submit()
        assert "Oops" in self.driver.page_source

    def test_6_invalid_first_name(self):
        self.driver.get("http://www.sandbox.opendrive.com/signup")
        assert "OpenDrive – OpenDrive Sign Up" in self.driver.title
        first_name = self.driver.find_element_by_id("signup-first-name")
        first_name.click()
        first_name.send_keys("J")
        last_name = self.driver.find_element_by_id("signup-last-name")
        last_name.click()
        last_name.send_keys("Doe")
        email = self.driver.find_element_by_id("signup-email")
        email.click()
        email.send_keys("qaautotestqa+1@gmail.com")
        password = self.driver.find_element_by_id("signup-password")
        password.click()
        password.send_keys("rootpass")
        password.submit()
        assert "Oops" in self.driver.page_source

    def test_7_invalid_last_name(self):
        self.driver.get("http://www.sandbox.opendrive.com/signup")
        assert "OpenDrive – OpenDrive Sign Up" in self.driver.title
        first_name = self.driver.find_element_by_id("signup-first-name")
        first_name.click()
        first_name.send_keys("John")
        last_name = self.driver.find_element_by_id("signup-last-name")
        last_name.click()
        last_name.send_keys("D")
        email = self.driver.find_element_by_id("signup-email")
        email.click()
        email.send_keys("qaautotestqa+1@gmail.com")
        password = self.driver.find_element_by_id("signup-password")
        password.click()
        password.send_keys("rootpass")
        password.submit()
        assert "Oops" in self.driver.page_source

    def test_8_invalid_email(self):
        self.driver.get("http://www.sandbox.opendrive.com/signup")
        assert "OpenDrive – OpenDrive Sign Up" in self.driver.title
        first_name = self.driver.find_element_by_id("signup-first-name")
        first_name.click()
        first_name.send_keys("John")
        last_name = self.driver.find_element_by_id("signup-last-name")
        last_name.click()
        last_name.send_keys("Doe")
        email = self.driver.find_element_by_id("signup-email")
        email.click()
        email.send_keys("qaautotestqa")
        password = self.driver.find_element_by_id("signup-password")
        password.click()
        password.send_keys("rootpass")
        password.submit()
        assert "Oops" in self.driver.page_source

    def test_9_invalid_email2(self):
        self.driver.get("http://www.sandbox.opendrive.com/signup")
        assert "OpenDrive – OpenDrive Sign Up" in self.driver.title
        first_name = self.driver.find_element_by_id("signup-first-name")
        first_name.click()
        first_name.send_keys("John")
        last_name = self.driver.find_element_by_id("signup-last-name")
        last_name.click()
        last_name.send_keys("Doe")
        email = self.driver.find_element_by_id("signup-email")
        email.click()
        email.send_keys("autotest@gmail.com")
        password = self.driver.find_element_by_id("signup-password")
        password.click()
        password.send_keys("rootpass")
        password.submit()
        assert "Oops" in self.driver.page_source

    def test_10_invalid_passwodr(self):
        self.driver.get("http://www.sandbox.opendrive.com/signup")
        assert "OpenDrive – OpenDrive Sign Up" in self.driver.title
        first_name = self.driver.find_element_by_id("signup-first-name")
        first_name.click()
        first_name.send_keys("John")
        last_name = self.driver.find_element_by_id("signup-last-name")
        last_name.click()
        last_name.send_keys("Doe")
        email = self.driver.find_element_by_id("signup-email")
        email.click()
        email.send_keys("autotest+1@gmail.com")
        password = self.driver.find_element_by_id("signup-password")
        password.click()
        password.send_keys("r")
        password.submit()
        assert "Oops" in self.driver.page_source

    def test_11_first_name_empty(self):
        self.driver.get("http://www.sandbox.opendrive.com/signup")
        assert "OpenDrive – OpenDrive Sign Up" in self.driver.title
        last_name = self.driver.find_element_by_id("signup-last-name")
        last_name.click()
        last_name.send_keys("Doe")
        email = self.driver.find_element_by_id("signup-email")
        email.click()
        email.send_keys("qaautotestqa+1@gmail.com")
        password = self.driver.find_element_by_id("signup-password")
        password.click()
        password.send_keys("rootpass")
        password.submit()
        assert "`first_name` is required." in self.driver.page_source

    def test_12_last_name_empty(self):
        self.driver.get("http://www.sandbox.opendrive.com/signup")
        assert "OpenDrive – OpenDrive Sign Up" in self.driver.title
        first_name = self.driver.find_element_by_id("signup-first-name")
        first_name.click()
        first_name.send_keys("John")
        email = self.driver.find_element_by_id("signup-email")
        email.click()
        email.send_keys("qaautotestqa+1@gmail.com")
        password = self.driver.find_element_by_id("signup-password")
        password.click()
        password.send_keys("rootpass")
        password.submit()
        assert "`last_name` is required." in self.driver.page_source

    def test_13_email_empty(self):
        self.driver.get("http://www.sandbox.opendrive.com/signup")
        assert "OpenDrive – OpenDrive Sign Up" in self.driver.title
        first_name = self.driver.find_element_by_id("signup-first-name")
        first_name.click()
        first_name.send_keys("John")
        last_name = self.driver.find_element_by_id("signup-last-name")
        last_name.click()
        last_name.send_keys("Doe")
        password = self.driver.find_element_by_id("signup-password")
        password.click()
        password.send_keys("rootpass")
        password.submit()
        assert "Oops" in self.driver.page_source

    def test_14_password_emty(self):
        self.driver.get("http://www.sandbox.opendrive.com/signup")
        assert "OpenDrive – OpenDrive Sign Up" in self.driver.title
        first_name = self.driver.find_element_by_id("signup-first-name")
        first_name.click()
        first_name.send_keys("John")
        last_name = self.driver.find_element_by_id("signup-last-name")
        last_name.click()
        last_name.send_keys("Doe")
        email = self.driver.find_element_by_id("signup-email")
        email.click()
        email.send_keys("autotest+1@gmail.com")
        email.submit()
        assert "`passwd` is required." in self.driver.page_source

    def test_15_valid_values(self):
        self.driver.get("http://www.sandbox.opendrive.com/signup")
        assert "OpenDrive – OpenDrive Sign Up" in self.driver.title
        first_name = self.driver.find_element_by_id("signup-first-name")
        first_name.click()
        first_name.send_keys(f.name())
        last_name = self.driver.find_element_by_id("signup-last-name")
        last_name.click()
        last_name.send_keys(f.name())
        email = self.driver.find_element_by_id("signup-email")
        email.click()
        email.send_keys(f.email())
        password = self.driver.find_element_by_id("signup-password")
        password.click()
        password.send_keys("rootpass")
        password.submit()
        assert "MyDrive" in self.driver.title

        self.driver.delete_all_cookies()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == '__main__':
        unittest.main(verbosity=2)

#qa password
