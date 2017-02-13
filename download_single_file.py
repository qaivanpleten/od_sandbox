import unittest, time, os, hashlib
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

fake_folder_name = Faker()


class download_file(unittest.TestCase):
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

    def test_3_download_file(self):
        find_container = wait.until(EC.element_to_be_clickable(
                    (By.ID, "file-NTFfMV9zWjNqRA")))
        menu = self.driver.find_element_by_xpath(
                ".//*[@id='file-NTFfMV9zWjNqRA']/div/i[3]")
        ActionChains(self.driver).move_to_element(find_container).move_to_element(menu).click(menu).perform()

        download_button = self.driver.find_element_by_xpath(".//*[@id='file-NTFfMV9zWjNqRA']/div/ul/li[1]/a")
        download_button.click()
        time.sleep(10)

    def test_4_check_file(self):
        # check file in folder
        self.assertTrue(os.path.exists("/home/developer/Загрузки/tumblr_of8n6x25FT1r2qr2so1_500.jpg"))

        # check size
        self.assertEqual(47072, (os.path.getsize("/home/developer/Загрузки/tumblr_of8n6x25FT1r2qr2so1_500.jpg")))

        # check hash
        self.assertEqual("08d17c81c3402ea485ddf31713c79fae",
                         (hashlib.md5(open("/home/developer/Загрузки/tumblr_of8n6x25FT1r2qr2so1_500.jpg",
                                           "rb").read()).hexdigest()))

        # delete file
        os.remove("/home/developer/Загрузки/tumblr_of8n6x25FT1r2qr2so1_500.jpg")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == '__main__':
        unittest.main(verbosity=2)


