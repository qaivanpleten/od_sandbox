import unittest, time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from faker import Faker
fake_folder_name = Faker()

class file_properties(unittest.TestCase):
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
        username.send_keys("qa.ivanpleten@gmail.com")
        password = self.driver.find_element_by_id("login_password")
        password.click()
        password.send_keys("rootpass")
        password.submit()
        self.assertIn("MyDrive", self.driver.title)                                   # check page title in HTML

    def test_2_create_file(self):
        if self.driver.find_element_by_xpath(".//*[@id='container']/div[11]/div[3]/div/div/i[5]").get_attribute("class")\
                != "fa fa-th view-mode js-change-view-mode active":

            # click grid view
            grid = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='container']/div[11]/div[3]/div/div/i[5]")))
            grid.click()
            time.sleep(3)
            self.assertEqual("fa fa-th view-mode js-change-view-mode active", self.driver.find_element_by_xpath(
                ".//*[@id='container']/div[11]/div[3]/div/div/i[5]").get_attribute("class"))

        else:
            pass

        # create txt file
        find_container = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='container']/div[11]/div[3]/div/div/ul/li/i")))
        create_text = self.driver.find_element_by_id("new-file-txt")
        ActionChains(self.driver).move_to_element(find_container).move_to_element(create_text).click().perform()
        time.sleep(4)
        file_txt = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='tabs-container']/div/div/div/div/label")))
        self.assertEqual("Text.txt", file_txt.get_attribute("title"))

    def test_3_edit_properties(self):
        file_txt = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='tabs-container']/div/div/div/div/label")))
        self.assertEqual("Text.txt", file_txt.get_attribute("title"))

        # open properties popup
        find_container = wait.until(
            EC.element_to_be_clickable((By.XPATH, ".//div[@class='js-tab-content tab-content scrollable folder']/div/div/div")))
        menu = self.driver.find_element_by_xpath(".//div[@class='js-tab-content tab-content scrollable folder']/div/div/div/i[3]")
        ActionChains(self.driver).move_to_element(find_container).move_to_element(menu).click().perform()
        properties_button = self.driver.find_element_by_xpath(
            ".//div[@class='js-tab-content tab-content scrollable folder']/div/div/div/ul/li[5]/a")
        properties_button.click()

        # change name
        file_name_input = wait.until(EC.element_to_be_clickable((By.ID, "prop-file-name")))
        file_name_input.click()
        file_name_input.clear()
        time.sleep(3)
        file_name_input.send_keys("rename file.txt")
        self.driver.find_element_by_id("prop-save-btn").click()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(4)
        self.assertEqual("rename file.txt", self.driver.find_element_by_xpath("//div[@class='tabs-container']/div/div/div/div/label").get_attribute("data-filename"))

    def test_4_edit_description(self):
        # open properties popup
        find_container = wait.until(
            EC.element_to_be_clickable((By.XPATH, ".//div[@class='js-tab-content tab-content scrollable folder']/div/div/div")))
        menu = self.driver.find_element_by_xpath(".//div[@class='js-tab-content tab-content scrollable folder']/div/div/div/i[3]")
        ActionChains(self.driver).move_to_element(find_container).move_to_element(menu).click().perform()
        properties_button = self.driver.find_element_by_xpath(
            ".//div[@class='js-tab-content tab-content scrollable folder']/div/div/div/ul/li[5]/a")
        properties_button.click()

        description_area = wait.until(EC.element_to_be_clickable((By.ID, "prop-file-description")))
        description_area.click()
        description_area.clear()
        description_area.send_keys("discriptioon")
        self.driver.find_element_by_id("prop-save-btn").click()
        time.sleep(3)


    def test_8_delete_file(self):
        # delete all files
        check_box = wait.until(
            EC.element_to_be_clickable((By.XPATH, ".//*[@id='container']/div[11]/div[3]/div/div/i[3]")))
        check_box.click()
        delete_button = wait.until(EC.element_to_be_clickable((By.ID, "menu-trash-btn")))
        delete_button.click()

        WebDriverWait(self.driver, 3).until(EC.alert_is_present(), "Do you really want to perform this action?")
        alert = self.driver.switch_to_alert()
        alert.accept()
        self.driver.delete_all_cookies()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


    if __name__ == '__main__':
        unittest.main(verbosity=2)