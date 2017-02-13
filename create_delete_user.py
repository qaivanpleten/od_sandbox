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
from selenium.webdriver.common.action_chains import ActionChains


class create_delete_edit_user(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://www.sandbox.opendrive.com/login")                   #Open page and wait
        cls.driver.title
        global wait
        wait = WebDriverWait(cls.driver, 15)


    # login
    def test_1_login(self):
        username = wait.until(EC.element_to_be_clickable((By.ID, "login_username")))
        username.click()
        username.send_keys("qa.ivanpleten@gmail.com")
        password = wait.until(EC.element_to_be_clickable((By.ID, "login_password")))
        password.click()
        password.send_keys("rootpass")
        password.submit()
        assert "MyDrive" in self.driver.page_source
        assert "https://sandbox.opendrive.com/files" in self.driver.current_url

    # go to users page
        user_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                             ".//*[@id='container']/div[11]/div[1]/div/a[4]")))
        user_button.click()
        self.assertEqual("https://sandbox.opendrive.com/users", self.driver.current_url)

    def test_2_create_users_group_create_user(self):
        create_us_gr_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                     ".//*[@id='container']/div[1]/div[10]/ul/li[1]/a[2]")))
        create_us_gr_button.click()
        group_name_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".group-rename")))
        group_name = fake.company()
        group_name_field.send_keys(group_name)
        time.sleep(3)
        group_name_field.send_keys(Keys.ENTER)
        time.sleep(3)
        global group_id
        group_id = self.driver.find_element_by_xpath(".//ul[@class='root-menu js-root-menu']/li[2]/ul/li").get_attribute("id")
        self.assertEqual(group_name, self.driver.find_element_by_xpath(
            ".//ul[@class='root-menu js-root-menu']/li[2]/ul/li/a/div/div[2]").get_attribute("textContent"))

    # create users
        i = 0
        while i < 10:
            create_us_button = wait.until(EC.element_to_be_clickable((By.ID, "new-user-btn")))
            create_us_button.click()
            new_user = wait. until(EC.element_to_be_clickable((By.XPATH,
                                                               ".//*[@id='container']/div[1]/div[13]/div/div/div[last()]/div[1]/span")))
            new_user.click()
            time.sleep(3)
            first_name = self.driver.find_element_by_xpath(".//*[@id='new-user-details-dropdown']/form/div[1]/input[1]")
            first_name.click()
            first_name.send_keys(fake.name())
            last_name = self.driver.find_element_by_xpath(".//*[@id='new-user-details-dropdown']/form/div[1]/input[2]")
            last_name.click()
            last_name.send_keys(fake.name())
            email = self.driver.find_element_by_xpath(".//*[@id='new-user-details-dropdown']/form/div[1]/input[3]")
            email.click()
            email.send_keys(fake.email())
            position = self.driver.find_element_by_xpath(".//*[@id='new-user-details-dropdown']/form/div[1]/input[4]")
            position.click()
            position.send_keys(fake.company())
            password = self.driver.find_element_by_xpath(".//*[@id='new-user-details-dropdown']/form/div[1]/input[5]")
            password.click()
            password.send_keys("rootpass")
            password.send_keys(Keys.RETURN)
            time.sleep(3)
            i += 1

    def test_3_activate_notifications(self):
        notfication_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                    ".//*[@id='container']/div[1]/div[13]/div/div/div[2]/div[3]/a[2]/i[2]")))
        self.assertEqual("email-notification-btn notifications-off",
                         self.driver.find_element_by_xpath(".//*[@id='container']/div[1]/div[13]/div/div/div[2]/div[3]/a[2]")
                         .get_attribute("class"))
        notfication_button.click()
        time.sleep(2)
        self.assertEqual("email-notification-btn notifications-on",
                         self.driver.find_element_by_xpath(".//*[@id='container']/div[1]/div[13]/div/div/div[2]/div[3]/a[2]")
                         .get_attribute("class"))

        self.driver.refresh()
        time.sleep(3)

    def test_4_change_storage_usage(self):
        storage_usage_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                      ".//*[@id='container']/div[1]/div[13]/div/div/div[2]/div[5]")))
        storage_usage_button.click()
        time.sleep(3)
        number_s = self.driver.find_element_by_id("account_user_storage")
        number_s.click()
        number_s.clear()
        number_s.send_keys("500")
        Select(self.driver.find_element_by_id("account_user_storage_units")).select_by_value("MB")
        self.driver.find_element_by_xpath(".//*[@id='container']/div[1]/div[13]/div/div/div/div").click()

    def test_5_change_Bandwidth_usage(self):
        bandwidth_usage_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                        ".//*[@id='container']/div[1]/div[13]/div/div/div[2]/div[6]")))
        bandwidth_usage_button.click()
        time.sleep(3)
        number_d = self.driver.find_element_by_id("account_user_bandwidth")
        number_d.click()
        number_d.clear()
        number_d.send_keys("500")
        Select(self.driver.find_element_by_id("account_user_bandwidth_units")).select_by_value("MB")
        self.driver.find_element_by_xpath(".//*[@id='container']/div[1]/div[13]/div/div/div/div").click()
        time.sleep(5)

    def test_6_delete_user(self):
        users_checkbox = wait.until(EC.element_to_be_clickable(
            (By.XPATH, ".//*[@id='container']/div/div[13]/div/div/div[2]/div[1]/div/i[1]")))
        users_checkbox.click()

        menu = wait.until(EC.element_to_be_clickable(
            (By.XPATH, ".//*[@id='container']/div/div[13]/div/div/div[1]/div[1]/div/ul/li/i")))
        delete_button = self.driver.find_element_by_id("users-delete-btn")
        ActionChains(self.driver).move_to_element(menu).move_to_element(delete_button).click(delete_button).perform()
        time.sleep(2)

        # delete
        wait.until(EC.alert_is_present(), "Do you really want to perform this action?")
        alert = self.driver.switch_to_alert()
        alert.accept()
        time.sleep(5)

    def test_7_block_user(self):
        self.driver.refresh()
        time.sleep(5)
        users_checkbox = wait.until(EC.element_to_be_clickable(
            (By.XPATH, ".//*[@id='container']/div/div[13]/div/div/div[2]/div[1]/div/i[1]")))
        #users_checkbox = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[13]/div/div/div[2]/div[1]/div/i[1]")
        users_checkbox.click()

        menu = wait.until(EC.element_to_be_clickable(
            (By.XPATH, ".//*[@id='container']/div/div[13]/div/div/div[1]/div[1]/div/ul/li/i")))
        block_button = self.driver.find_element_by_id("users-block-btn")
        ActionChains(self.driver).move_to_element(menu).move_to_element(block_button).click(block_button).perform()
        time.sleep(2)

        self.assertEqual("user-row draggable col-md-12 col-sm-12  ui-draggable blocked",
                         self.driver.find_element_by_xpath(".//*[@id='container']/div/div[13]/div/div/div[2]")
                         .get_attribute("class"))

    def test_7_delete_users_group(self):
        # delete users group
        self.driver.refresh()
        find_users_group = wait.until(EC.element_to_be_clickable(
            (By.XPATH, ".//*[@id='" + group_id + "']/a/div")))
            #self.driver.find_element_by_css_selector(".group-name.js-folder-name")
        menu = self.driver.find_element_by_xpath(".//*[@id='" + group_id + "']/i[2]")
        delete_button = self.driver.find_element_by_xpath(".//*[@id='" + group_id + "']/ul/li[3]/a")
        ActionChains(self.driver).move_to_element(find_users_group)\
            .move_to_element(menu).click(menu).perform()
        delete_button.click()
        time.sleep(2)

        # delete
        wait.until(EC.alert_is_present(), "Do you really want to perform this action?")
        alert = self.driver.switch_to_alert()
        alert.accept()
        self.driver.delete_all_cookies()
        time.sleep(3)



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == '__main__':
        unittest.main(verbosity=2)