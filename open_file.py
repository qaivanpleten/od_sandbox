import unittest, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from faker import Faker

fake = Faker()

class open_file(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://www.sandbox.opendrive.com/login")                   #Open page and wait
        cls.driver.title
        global wait
        wait = WebDriverWait(cls.driver, 15)

    def test_1_login(self):
        username = wait.until(EC.element_to_be_clickable((By.ID, "login_username")))
        username.click()
        username.send_keys("qa.ivanpleten+test@gmail.com")
        password = wait.until(EC.element_to_be_clickable((By.ID, "login_password")))
        password.click()
        password.send_keys("rootpass")
        password.submit()
        self.assertIn("MyDrive", self.driver.page_source)
        self.assertIn("https://sandbox.opendrive.com/files", self.driver.current_url)

    def test_2_open_pdf_file(self):
        pdf_file = wait.until(EC.element_to_be_clickable((By.ID, "file-MzBfMTM5X3lXSlU5")))
        pdf_file.click()

        # check url
        self.assertIn("https://sandbox.opendrive.com/file/MzBfMTM5X3lXSlU5", self.driver.current_url)
        # check tab
        self.assertIn("js-item-tab active tab-loaded",
                      self.driver.find_element_by_xpath(".//*[@id='container']/header/div/div[3]/ul/li[2]").
                      get_attribute("class"))

        self.assertIn("file-MzBfMTM5X3lXSlU5",
                  self.driver.find_element_by_xpath(".//*[@id='container']/header/div/div[3]/ul/li[2]").
                  get_attribute("data-itemid"))

        # close tab
        self.driver.find_element_by_xpath(".//*[@id='container']/header/div/div[3]/ul/li[2]/a[2]").click()
        # check tab
        self.assertIn("js-item-tab tab-loaded active",
                      self.driver.find_element_by_xpath(".//*[@id='container']/header/div/div[3]/ul/li").
                      get_attribute("class"))


    def test_3_open_picture(self):
        picture_file = wait.until(EC.element_to_be_clickable((By.ID, "file-MzBfMTI4X2JjZ0cw")))
        picture_file.click()

        # check url
        self.assertIn("https://sandbox.opendrive.com/file/MzBfMTI4X2JjZ0cw", self.driver.current_url)
        # check tab
        self.assertIn("js-item-tab active tab-loaded",
                      self.driver.find_element_by_xpath(".//*[@id='container']/header/div/div[3]/ul/li[2]").
                      get_attribute("class"))

        self.assertIn("file-MzBfMTI4X2JjZ0cw",
                  self.driver.find_element_by_xpath(".//*[@id='container']/header/div/div[3]/ul/li[2]").
                  get_attribute("data-itemid"))

    def test_4_open_zip(self):
        self.driver.find_element_by_xpath(".//*[@id='container']/header/div/div[3]/ul/li[1]/a").click()
        # check tab
        self.assertIn("js-item-tab tab-loaded active",
                      self.driver.find_element_by_xpath(".//*[@id='container']/header/div/div[3]/ul/li").
                      get_attribute("class"))

        zip_file = wait.until(EC.element_to_be_clickable((By.ID, "file-MzBfMTQ1X0s1cHdS")))
        zip_file.click()

        # check url
        self.assertIn("https://sandbox.opendrive.com/file/MzBfMTQ1X0s1cHdS", self.driver.current_url)
        # check tab
        self.assertIn("js-item-tab active tab-loaded",
                      self.driver.find_element_by_xpath(".//*[@id='container']/header/div/div[3]/ul/li[3]").
                      get_attribute("class"))

        self.assertIn("file-MzBfMTQ1X0s1cHdS",
                  self.driver.find_element_by_xpath(".//*[@id='container']/header/div/div[3]/ul/li[3]").
                  get_attribute("data-itemid"))

    def test_5_open_mp3(self):
        self.driver.find_element_by_xpath(".//*[@id='container']/header/div/div[3]/ul/li[1]/a").click()
        # check tab
        self.assertIn("js-item-tab tab-loaded active",
                      self.driver.find_element_by_xpath(".//*[@id='container']/header/div/div[3]/ul/li").
                      get_attribute("class"))

        mp3_file = wait.until(EC.element_to_be_clickable((By.ID, "file-MzBfMTEyX0NSQXFz")))
        mp3_file.click()

        # check url
        self.assertIn("https://sandbox.opendrive.com/file/MzBfMTEyX0NSQXFz", self.driver.current_url)
        # check tab
        self.assertIn("js-item-tab active tab-loaded",
                      self.driver.find_element_by_xpath(".//*[@id='container']/header/div/div[3]/ul/li[4]").
                      get_attribute("class"))

        self.assertIn("file-MzBfMTEyX0NSQXFz",
                  self.driver.find_element_by_xpath(".//*[@id='container']/header/div/div[3]/ul/li[4]").
                  get_attribute("data-itemid"))

    def test_6_check_tabs(self):
        i = 0
        while i < 10:
            # go to overview
            self.driver.find_element_by_xpath(".//*[@id='container']/header/div/div[3]/ul/li[1]/a").click()
            # check tab
            self.assertIn("js-item-tab tab-loaded active",
                          self.driver.find_element_by_xpath(".//*[@id='container']/header/div/div[3]/ul/li").
                          get_attribute("class"))

            # go to second tab
            self.driver.find_element_by_xpath(".//*[@id='container']/header/div/div[3]/ul/li[2]/a[1]").click()
            # check tab
            self.assertIn("js-item-tab tab-loaded active",
                          self.driver.find_element_by_xpath(".//*[@id='container']/header/div/div[3]/ul/li[2]").
                          get_attribute("class"))

            # go to third tab
            self.driver.find_element_by_xpath(".//*[@id='container']/header/div/div[3]/ul/li[3]/a[1]").click()
            # check tab
            self.assertIn("js-item-tab tab-loaded active",
                          self.driver.find_element_by_xpath(".//*[@id='container']/header/div/div[3]/ul/li[3]").
                          get_attribute("class"))

            # go to fourth tab
            self.driver.find_element_by_xpath(".//*[@id='container']/header/div/div[3]/ul/li[4]/a[1]").click()
            # check tab
            self.assertIn("js-item-tab tab-loaded active",
                          self.driver.find_element_by_xpath(".//*[@id='container']/header/div/div[3]/ul/li[4]").
                          get_attribute("class"))
            i += 1

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == '__main__':
        unittest.main(verbosity=2)
