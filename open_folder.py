import unittest, time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from faker import Faker
fake_folder_name = Faker()

class open_folder(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()                                  #can use Firefox or Chrome
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.title
        self.driver.get("http://www.sandbox.opendrive.com/login")          #navigation to login page

    def test_open_folder(self):
        wait = WebDriverWait(self.driver, 10)

        username = self.driver.find_element_by_id("login_username")
        username.click()
        username.send_keys("qa.ivanpleten@gmail.com")
        password = self.driver.find_element_by_id("login_password")
        password.click()
        password.send_keys("rootpass")
        password.submit()
        self.assertIn("MyDrive", self.driver.title)                                   # check page title in HTML

    #create folder
        self.driver.get("http://www.sandbox.opendrive.com/files")
        self.driver.find_element_by_xpath('//div[@class="fill"]/div/ul/li/a[@title="Create Folder"]').click()
        folder_name = self.driver.find_element_by_xpath('//ul[@class="folders-in-root items-container js-root-menu-items ps-container ps-theme-od"]/li[last()]/a/span')
        fake_name = fake_folder_name.company()
        folder_name.send_keys(fake_name)
        folder_name.send_keys(Keys.RETURN)
        time.sleep(3)
        folder_id = self.driver.find_element_by_xpath(".//ul[@class='root-menu js-root-menu']/li[2]/ul/li").get_attribute("id")

    #open folder
        open_folder = wait.until(EC.element_to_be_clickable((By.ID, folder_id)))     # click on folder -> open folder
        open_folder.click()
        time.sleep(3)
        self.assertEqual(folder_id, self.driver.find_element_by_xpath(".//*[@id='container']/div[11]/div[3]/div").get_attribute("data-itemid"))
        icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".root-dir.js-root-dir.ellipsis_overflow.ui-droppable")))
        icon.click()
        time.sleep(3)
        self.assertEqual("MyDrive", self.driver.find_element_by_xpath(".//*[@id='container']/header/div/div[3]/ul/li/a").get_attribute("title"))
        folder2 = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='"+ folder_id + "']/div/a/i")))
        folder2.click()
        time.sleep(3)
        self.assertEqual(folder_id, self.driver.find_element_by_xpath(".//*[@id='container']/div[11]/div[3]/div").get_attribute("data-itemid"))
        time.sleep(3)
        icon.click()
        time.sleep(3)
        self.assertIn("https://sandbox.opendrive.com/files", self.driver.current_url)

    #list view
        list_view_button = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='container']/div[11]/div[3]/div/div/i[6]")))
        list_view_button.click()
        time.sleep(3)
        self.assertEqual("fa fa-list view-mode js-change-view-mode active", self.driver.find_element_by_xpath(
            ".//*[@id='container']/div[11]/div[3]/div/div/i[6]").get_attribute("class"))

    #open folder
        #folder = wait.until(EC.element_to_be_clickable((By.XPATH, ".//div[@class='js-tab-content tab-content scrollable folder']/div[2]/div/div[2]/div[1]")))
        open_folder.click()
        time.sleep(3)
        self.assertEqual(folder_id, self.driver.find_element_by_xpath(
            ".//*[@id='container']/header/div/div[3]/ul/li").get_attribute("data-itemid"))
        # icon.click()
        # time.sleep(3)
        # self.assertEqual("MyDrive", self.driver.find_element_by_xpath(
        #     ".//*[@id='container']/header/div/div[3]/ul/li/a").get_attribute("title"))

    #grid view
        grid = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='container']/div[11]/div[3]/div/div/i[5]")))
        grid.click()
        time.sleep(3)
        self.assertEqual("fa fa-th view-mode js-change-view-mode active", self.driver.find_element_by_xpath(
            ".//*[@id='container']/div[11]/div[3]/div/div/i[5]").get_attribute("class"))

    # go to main folder
        icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".root-dir.js-root-dir.ellipsis_overflow.ui-droppable")))
        icon.click()
        time.sleep(3)
        self.assertEqual("MyDrive", self.driver.find_element_by_xpath(
            ".//*[@id='container']/header/div/div[3]/ul/li/a").get_attribute("title"))

    # delete all files
        check_box = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='container']/div[11]/div[3]/div/div/i[3]")))
        check_box.click()
        delete_button = wait.until(EC.element_to_be_clickable((By.ID, "menu-trash-btn")))
        delete_button.click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present(), "Do you really want to perform this action?")
        alert = self.driver.switch_to_alert()
        alert.accept()
        self.driver.delete_all_cookies()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main(verbosity=2)
