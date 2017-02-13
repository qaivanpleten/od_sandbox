import unittest, time, os, hashlib
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from faker import Faker
fake_folder_name = Faker()

class download_all(unittest.TestCase):
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
        self.assertIn("MyDrive - Login", self.driver.title)                             # check page title in HTML
        username = self.driver.find_element_by_id("login_username")
        username.click()
        username.send_keys("qa.ivanpleten+zip@gmail.com")
        password = self.driver.find_element_by_id("login_password")
        password.click()
        password.send_keys("rootpass")
        password.submit()
        self.assertIn("MyDrive", self.driver.title)

    def test_2_open_folder(self):
        download_all_folder = self.driver.find_element_by_id("folder-NTFfMzBfRGwzSGE")
        download_all_folder.click()
        time.sleep(2)
        self.assertIn("https://sandbox.opendrive.com/files/NTFfMzBfRGwzSGE", self.driver.current_url)

    def test_3_download_all(self):
        select_all_button = self.driver.\
            find_element_by_xpath(".//*[@id='container']/div[11]/div[3]/div/div/i[3]")
        select_all_button.click()
        download_button = self.driver.find_element_by_id("menu-download-btn")
        download_button.click()

        wait.until(EC.alert_is_present(), "Do you really want to perform this action?")
        alert = self.driver.switch_to_alert()
        alert.accept()
        time.sleep(40)

    def test_4_check_zip(self):
        # check file in folder
        self.assertTrue(os.path.exists("/home/developer/Загрузки/download all files and folders.zip"))

        # check size
        self.assertEqual(13092349,
                         (os.path.getsize("/home/developer/Загрузки/download all files and folders.zip")))

        # check hash
        self.assertEqual("489db2454b3005a95452cb96cb9c845d",
                         (hashlib.md5(open("/home/developer/Загрузки/download all files and folders.zip",
                                           "rb").read()).hexdigest()))

        # delete file
        os.remove("/home/developer/Загрузки/download all files and folders.zip")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == '__main__':
        unittest.main(verbosity=2)