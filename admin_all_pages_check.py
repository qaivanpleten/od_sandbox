import unittest, time, random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from faker import Faker
fake = Faker()

class admin_all_pages_check(unittest.TestCase):
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
        self.assertIn("MyDrive - Login", self.driver.title)
        username = self.driver.find_element_by_id("login_username")
        username.click()
        username.send_keys("alex_d")
        password = self.driver.find_element_by_id("login_password")
        password.click()
        password.send_keys("qwertz")
        password.submit()
        self.assertIn("https://sandbox.opendrive.com/files/", self.driver.current_url)

        # go to admin page
        admin_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".fa.fa-user-secret")))
        admin_button.click()
        self.assertIn("https://sandbox.opendrive.com/admin/users", self.driver.current_url)

        #check title in sidebar
        self.assertIn("Admin",
                      self.driver.find_element_by_xpath(".//*[@id='container']/div/div[3]/ul/li[1]/a").get_attribute("textContent"))

        #check button in sidebar is active
        self.assertIn("item active",
                      self.driver.find_element_by_xpath(".//*[@id='container']/div/div[3]/ul/li[2]/ul/li[1]").get_attribute("class"))


    def test_2_check_dashboard_page(self):
        dashboard_button = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[3]/ul/li[2]/ul/li[2]/a/i")
        dashboard_button.click()

        #check url
        self.assertIn("https://sandbox.opendrive.com/admin/partners", self.driver.current_url)

        #check activ button in sidebar
        self.assertIn("item active admin-partners",
                      self.driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/ul/li[2]/ul/div/div/li[2]")
                      .get_attribute("class"))

        # check elements
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div/div/div[1]/div")
                        .is_displayed())

        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div/div/div[2]/div")
                        .is_displayed())

        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div/div/div[3]/div")
                        .is_displayed())

        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div/div/div[4]/div")
                        .is_displayed())

        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div/div/div[6]")
                        .is_displayed())

        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div/div/div[7]")
                        .is_displayed())

    def test_3_check_transaction_page(self):
        transaction_button = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/ul/li[2]/ul/div/div/li[3]/a/i")
        transaction_button.click()

        #check url
        self.assertIn("https://sandbox.opendrive.com/admin/transactions", self.driver.current_url)

        #check activ button in sidebar
        self.assertIn("item active",
                      self.driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/ul/li[2]/ul/li[3]")
                      .get_attribute("class"))

        # check elements
        self.assertTrue(self.driver.find_element_by_id("tab-transactions-content")
                        .is_displayed())

    def test_4_check_maintenance_page(self):
        maintenance_button = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/ul/li[2]/ul/li[4]/a/i")
        maintenance_button.click()

        #check url
        self.assertIn("https://sandbox.opendrive.com/admin/maintenance", self.driver.current_url)

        #check activ button in sidebar
        self.assertIn("item active",
                      self.driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/ul/li[2]/ul/li[4]")
                      .get_attribute("class"))

        # check elements
        z = 1
        while z < 7:
            self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div[" + str(z) +"]/div")
                        .is_displayed())

            z += 1

    def test_5_check_funcrional(self):
        # trash item of closed accounts
        trash_item_button = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div[1]/div/a")
        trash_item_button.click()
        self.assertIn("Operation has been successfully completed",
                      self.driver.find_element_by_xpath("html/body/div[3]/div/div[2]")
                      .get_attribute("textContent"))
        time.sleep(5)

        # Reset bandwidth of all users
        reset_bandwidth_button = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div[2]/div/a")
        reset_bandwidth_button.click()
        self.assertIn("Operation has been successfully completed",
                      self.driver.find_element_by_xpath("html/body/div[3]/div/div[2]")
                      .get_attribute("textContent"))
        time.sleep(5)

        # Remove files of basic users not logged for more than 6 months
        remove_files_button = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div[3]/div/a")
        remove_files_button.click()
        self.assertIn("Operation has been successfully completed",
                      self.driver.find_element_by_xpath("html/body/div[3]/div/div[2]")
                      .get_attribute("textContent"))
        time.sleep(5)

        # Clear automatically replaced files
        clear_replaced_button = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div[4]/div/a")
        clear_replaced_button.click()
        self.assertIn("Operation has been successfully completed",
                      self.driver.find_element_by_xpath("html/body/div[3]/div/div[2]")
                      .get_attribute("textContent"))
        time.sleep(5)

        # Clear from DB deleted folders
        clear_from_db_button = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div[5]/div/a")
        clear_from_db_button.click()
        self.assertIn("Operation has been successfully completed",
                      self.driver.find_element_by_xpath("html/body/div[3]/div/div[2]")
                      .get_attribute("textContent"))
        time.sleep(5)

        # Send reminder to users suspended for more than 90 days
        send_reminder_button = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div[6]/div/a")
        send_reminder_button.click()
        self.assertIn("Operation has been successfully completed",
                      self.driver.find_element_by_xpath("html/body/div[3]/div/div[2]")
                      .get_attribute("textContent"))
        time.sleep(5)

        # Trash files of suspended users and downgrade to Basic plan
        trash_files_button = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div[7]/div/a")
        trash_files_button.click()
        self.assertIn("Operation has been successfully completed",
                      self.driver.find_element_by_xpath("html/body/div[3]/div/div[2]")
                      .get_attribute("textContent"))
        time.sleep(5)


    def test_6_check_manage_partitions(self):
        manage_partitions_button = self.driver.find_element_by_xpath(
            ".//*[@id='container']/div/div[2]/ul/li[2]/ul/li[5]/a/i")
        manage_partitions_button.click()

        # check url
        self.assertIn("https://sandbox.opendrive.com/admin/partitions", self.driver.current_url)

        # check active button in sidebar
        self.assertIn("item active",
                          self.driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/ul/li[2]/ul/li[5]")
                          .get_attribute("class"))
        time.sleep(2)
        # check elements
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div")
                            .is_displayed())


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


    if __name__ == '__main__':
        unittest.main(verbosity=2)