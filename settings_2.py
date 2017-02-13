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

class settings_change_2(unittest.TestCase):
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
        username.send_keys("qa.ivanpleten@gmail.com")
        password = wait.until(EC.element_to_be_clickable((By.ID, "login_password")))
        password.click()
        password.send_keys("rootpass")
        password.submit()
        self.assertIn("MyDrive", self.driver.page_source)
        self.assertIn("https://sandbox.opendrive.com/files", self.driver.current_url)

    # go to settings page
        settings_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                             ".//*[@id='container']/div[11]/div[1]/div/div/a[1]")))
        settings_button.click()
        self.assertIn("https://sandbox.opendrive.com/settings", self.driver.current_url)

        self.assertIn("Dashboard", self.driver.find_element_by_xpath(".//*[@id='container']/div/div[3]/h2/a").get_attribute("text"))

        self.assertIn("item active settings-plan",
                      self.driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/ul/li[2]/ul/div/div/li[1]").get_attribute("class"))

    def test_2_go_to_branding_page(self):
        branding_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                  ".//*[@id='container']/div/div[2]/ul/li[2]/ul/div/div/li[3]")))
        branding_button.click()
        self.assertIn("https://sandbox.opendrive.com/settings/branding", self.driver.current_url)
        self.assertIn("Branding",
                      self.driver.find_element_by_xpath(".//*[@id='container']/div/div[3]/h2/a").get_attribute("text"))
        self.assertIn("item active settings-branding",
                      self.driver.find_element_by_xpath(
                          ".//*[@id='container']/div/div[2]/ul/li[2]/ul/div/div/li[3]").get_attribute("class"))

        # the presence of elements on the page
        self.assertTrue(self.driver.find_element_by_xpath(
            ".//*[@id='container']/div/div[4]/div/div/div[1]/div[1]").is_displayed())
        self.assertIn("Logo",
                      self.driver.find_element_by_xpath(
                          ".//*[@id='container']/div/div[4]/div/div/div[1]/div[1]/h3").get_attribute(
                          "textContent"))

        self.assertTrue(self.driver.find_element_by_xpath(
            ".//*[@id='container']/div/div[4]/div/div/div[1]/div[2]").is_displayed())
        self.assertIn("Favicon",
                      self.driver.find_element_by_xpath(
                          ".//*[@id='container']/div/div[4]/div/div/div[1]/div[2]/h3").get_attribute(
                          "textContent"))

    def test_3_go_to_activity_page(self):
        settings_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                 ".//*[@id='container']/div/div[2]/ul/li[2]/ul/div/div/li[4]/a")))
        settings_button.click()
        self.assertIn("https://sandbox.opendrive.com/settings/activity", self.driver.current_url)

        self.assertIn("Activity Logs",
                      self.driver.find_element_by_xpath(".//*[@id='container']/div/div[3]/h2/a").get_attribute("text"))

        self.assertIn("item active settings-activity",
                      self.driver.find_element_by_xpath(
                          ".//*[@id='container']/div/div[2]/ul/li[2]/ul/div/div/li[4]").get_attribute("class"))
        # the presence of elements on the page
        self.assertTrue(self.driver.find_element_by_xpath(
            ".//*[@id='container']/div/div[4]/div/div").is_displayed())

    def test_4_logs_check(self):
        #september 15, 2016
        start = wait.until(EC.element_to_be_clickable((By.ID, "activity_start_date")))
        start.click()
        start_month = self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/span[1]").get_attribute(
            "textContent")
        start_year = self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/span[2]").get_attribute(
            "textContent")
        # print(start_month + start_year)

        while start_month != "June" or start_year != "2016":
            start = wait.until(EC.element_to_be_clickable((By.ID, "activity_start_date")))
            start.click()
            back_button = self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/a[1]/span")
            back_button.click()
            start_month = self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/span[1]").get_attribute("textContent")
            start_year = self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/span[2]").get_attribute("textContent")
            time.sleep(1)

            #print(start_month + start_year)

        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[3]/td[4]/a").click()

        ## september 16, 2016
        finish = wait.until(EC.element_to_be_clickable((By.ID, "activity_end_date")))
        finish.click()
        finish_month = self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/span[1]").get_attribute(
            "textContent")
        finish_year = self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/span[2]").get_attribute(
            "textContent")
        print(finish_month + finish_year)

        while finish_month != "June" or finish_year != "2016":
            finish = wait.until(EC.element_to_be_clickable((By.ID, "activity_end_date")))
            finish.click()
            back_button = self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/a[1]/span")
            back_button.click()
            finish_month = self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/span[1]").get_attribute("textContent")
            finish_year = self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/span[2]").get_attribute("textContent")
            time.sleep(1)

            #print(finish_month + finish_year)

        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[3]/td[5]/a").click()

        # change Log Type
        Select(self.driver.find_element_by_id("activity_log_type")).select_by_value("9000")
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='activity_log_type']/option[2]").is_selected())
        # show logs
        self.driver.find_element_by_id("activity-logs-form").click()
        # check result
        """self.assertIn("176.241.128.228",
                      self.driver.find_element_by_xpath(
                          ".//*[@id='container']/div/div[4]/div/div/div[2]/div/div/div[2]/div[4]").get_attribute("textContent"))"""

        """self.assertIn("USER LOGIN",
                      self.driver.find_element_by_xpath(
                          ".//*[@id='container']/div/div[4]/div/div/div[2]/div/div/div[2]/div[3]").get_attribute("textContent"))"""

        """self.assertIn("\n\t\t\t\t                        Jun 16, 2016, 01:32pm\t\t\t\t                    ",
                      self.driver.find_element_by_xpath(
                          ".//*[@id='container']/div/div[4]/div/div/div[2]/div/div/div[2]/div[1]").get_attribute(
                          "textContent"))"""

        #time.sleep(10)

    def test_5_upgrade_page(self):
        update_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                               ".//*[@id='container']/div/div[2]/ul/li[2]/ul/div/div/li[5]/a")))
        # go to upgrade page
        update_button.click()
        self.assertIn("https://sandbox.opendrive.com/billing/upgrade", self.driver.current_url)

        self.assertIn("Upgrade",
                      self.driver.find_element_by_xpath(".//*[@id='container']/div/div[6]/h2/a").get_attribute("text"))

        # Upgrade button in sidebar is active
        self.assertIn("item active billing-upgrade",
                      self.driver.find_element_by_xpath(
                          ".//*[@id='container']/div/div[2]/ul/li[2]/ul/div/div/li[5]").get_attribute("class"))
        # business plan is active
        self.assertIn("plan-tab active",
                      self.driver.find_element_by_xpath(".//*[@id='container']/div/div[7]/div/div/div[1]/a[2]")
                      .get_attribute("class"))

        # the presence of elements on the page
        a = 1
        while a < 4:
            cards_list = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[7]/div/div/div[2]/div[3]/div["+ str(a) +"]/div")
            self.assertTrue((cards_list).is_displayed())
            a += 1

        # go to personal plan
        personal_plan_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                               ".//*[@id='container']/div/div[7]/div/div/div[1]/a[1]")))
        personal_plan_button.click()

        # personal plan is active
        self.assertIn("plan-tab active",
                      self.driver.find_element_by_xpath(".//*[@id='container']/div/div[7]/div/div/div[1]/a[1]")
                      .get_attribute("class"))

        # the presence of elements on the page
        b = 1
        while b < 3:
            cards_list = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[7]/div/div/div[2]/div[2]/div["+ str(b) +"]/div")
            self.assertTrue((cards_list).is_displayed())
            b += 1

    def test_6_promocode_percent(self):
        promocode_field = self.driver.find_element_by_name("promocode")
        promocode_field.click()
        promocode_field.clear()
        promocode_field.send_keys("dealspl10")
        self.driver.find_element_by_class_name("promocode_btn").click()
        time.sleep(3)
        self.assertIn("Pricing with discount 10%",
                      self.driver.find_element_by_xpath(".//*[@id='container']/div/div[6]/div/form/strong")
                      .get_attribute("textContent"))

    def test_7_payment_methods_page(self):
        # go to Payment Methods page
        payment_methods_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                               ".//*[@id='container']/div/div[2]/ul/li[2]/ul/div/div/li[6]/a")))
        payment_methods_button.click()
        self.assertIn("https://sandbox.opendrive.com/billing/payments", self.driver.current_url)

        self.assertIn("Payment Methods",
                      self.driver.find_element_by_xpath(".//*[@id='container']/div/div[6]/h2/a").get_attribute("text"))

        # Upgrade button in sidebar is active
        self.assertIn("item active billing-payments",
                      self.driver.find_element_by_xpath(
                          ".//*[@id='container']/div/div[2]/ul/li[2]/ul/div/div/li[6]").get_attribute("class"))

    def test_8_promocode_dollar(self):
        # go to upgrade page

        update_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                               ".//*[@id='container']/div/div[2]/ul/li[2]/ul/div/div/li[5]/a")))
        update_button.click()
        self.assertIn("https://sandbox.opendrive.com/billing/upgrade", self.driver.current_url)

        self.assertIn("Upgrade",
                      self.driver.find_element_by_xpath(".//*[@id='container']/div/div[6]/h2/a").get_attribute("text"))

        promocode_field = self.driver.find_element_by_name("promocode")
        promocode_field.click()
        promocode_field.clear()
        promocode_field.send_keys("testdiscount3")
        self.driver.find_element_by_class_name("promocode_btn").click()
        time.sleep(3)
        self.assertIn("Pricing with discount 3$",
                      self.driver.find_element_by_xpath(".//*[@id='container']/div/div[6]/div/form/strong")
                      .get_attribute("textContent"))


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == '__main__':
        unittest.main(verbosity=2)