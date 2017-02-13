import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from faker import Faker
f = Faker()
from selenium.webdriver.common.action_chains import ActionChains

class delete_folder(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()                                  #can use Firefox or Chrome
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.title
        self.mouse = webdriver.ActionChains(self.driver)
        self.driver.get("http://www.sandbox.opendrive.com/login")          #navigation to login page

    #login
    def test_delete_folder(self):
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
        fake_folder_name = f.company()
        folder_name.send_keys(fake_folder_name)
        folder_name.send_keys(Keys.RETURN)
        time.sleep(3)
        self.assertEqual(fake_folder_name, self.driver.find_element_by_xpath("//div[@class='tabs-container']/div/div/div/div/label").get_attribute("title"))

        find_folder = self.driver.find_element_by_xpath(".//div[@class='js-tab-content tab-content scrollable folder']/div/div/div/a")
        menu = self.driver.find_element_by_xpath(".//div[@class='js-tab-content tab-content scrollable folder']/div/div/div/i[3]")

        action = ActionChains(self.driver).move_to_element(find_folder).move_to_element(menu)
        time.sleep(3)
        action.click(menu).perform()
        time.sleep(3)
        trash = self.driver.find_element_by_xpath(
            ".//div[@class='js-tab-content tab-content scrollable folder']/div/div/div/ul/li[7]/a")
        trash.click()
        time.sleep(3)

        #delete
        WebDriverWait(self.driver, 3).until(EC.alert_is_present(), "Do you really want to perform this action?")
        alert = self.driver.switch_to_alert()
        alert.accept()
        self.driver.delete_all_cookies()
        time.sleep(5)


    def tearDown(self):
        self.driver.close()


    if __name__ == '__main__':
        unittest.main()

