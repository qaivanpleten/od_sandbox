import unittest, time, os, hashlib
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from faker import Faker

fake_folder_name = Faker()


class download_folders(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://www.sandbox.opendrive.com/login")  # Open page and wait
        cls.driver.title
        global wait
        wait = WebDriverWait(cls.driver, 15)

    def test_1_login(self):
        self.assertIn("MyDrive - Login", self.driver.title)  # check page title in HTML
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
        file_id_list = ["folder-NTFfMzFfOEJzc1Y", "folder-NTFfMzJfYWROZ20", "folder-NTFfMzNfc01pMVE"]
        for id in file_id_list:
            find_container = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, ".//*[@id='" + id + "']/div")))
            checkbox = self.driver.find_element_by_xpath(
                ".//*[@id='" + id + "']/div/i[2]")
            ActionChains(self.driver).move_to_element(find_container).move_to_element(checkbox).click(checkbox).perform()

        download_button = self.driver.find_element_by_id("menu-download-btn")
        download_button.click()

        wait.until(EC.alert_is_present(), "Do you really want to perform this action?")
        alert = self.driver.switch_to_alert()
        alert.accept()
        time.sleep(50)

    def test_4_check_zip(self):
        # check file in folder
        self.assertTrue(os.path.exists("/home/developer/Загрузки/download all files and folders.zip"))

        # check size
        self.assertEqual(12202483,
                         (os.path.getsize("/home/developer/Загрузки/download all files and folders.zip")))

        # check hash
        self.assertEqual("4930b8eed17b624a326315fd4e91823c",
                         (hashlib.md5(open("/home/developer/Загрузки/download all files and folders.zip",
                                           "rb").read()).hexdigest()))
        # delete file
        os.remove("/home/developer/Загрузки/download all files and folders.zip")


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == '__main__':
        unittest.main(verbosity=2)