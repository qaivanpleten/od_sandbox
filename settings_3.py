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

class settings_change_3(unittest.TestCase):
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

    def test_2_go_to_payment_method_page(self):
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

    def test_3_add_card(self):
        add_card_button = wait.until(EC.element_to_be_clickable((By.ID,
                                                                 "settings-new-card")))
        add_card_button.click()

        # popup is visible
        self.assertTrue(self.driver.find_element_by_xpath(
            ".//*[@id='add-new-card']/div[2]/div[1]").is_displayed())

        # fill the form

        first_name = self.driver.find_element_by_id("new_card_firstname")
        first_name.click()
        first_name.clear()
        first_name.send_keys("John")

        last_name = self.driver.find_element_by_id("new_card_lastname")
        last_name.click()
        last_name.clear()
        last_name.send_keys("Doe")

        # card_type select
        Select(self.driver.find_element_by_id("new_card_type")).select_by_value("2")
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='new_card_type']/option[@value='2']").is_selected())

        card_number = self.driver.find_element_by_id("new_card_no")
        card_number.click()
        card_number.clear()
        card_number.send_keys("5555555555554444")

        Select(self.driver.find_element_by_id("new_card_exp_month")).select_by_value("05")
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='new_card_exp_month']/option[@value='05']").is_selected())

        Select(self.driver.find_element_by_id("new_card_exp_year")).select_by_value("2020")
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='new_card_exp_year']/option[@value='2020']").is_selected())

        secure_code = self.driver.find_element_by_id("new_card_cvc")
        secure_code.click()
        secure_code.clear()
        secure_code.send_keys("123")

        adress = self.driver.find_element_by_id("new_card_address")
        adress.click()
        adress.clear()
        adress.send_keys("Lorem")

        city = self.driver.find_element_by_id("new_card_city")
        city.click()
        city.clear()
        city.send_keys("Lorem")

        postal_code = self.driver.find_element_by_id("new_card_zip")
        postal_code.click()
        postal_code.clear()
        postal_code.send_keys("11111")

        state = self.driver.find_element_by_id("new_card_state")
        state.click()
        state.clear()
        state.send_keys("Lorem")

        Select(self.driver.find_element_by_id("new_card_country")).select_by_value("108")
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='new_card_country']/option[@value='108']").is_selected())

        # save
        save_button = self.driver.find_element_by_id("add-new-card-btn")
        save_button.click()

        global card_id
        card_id = self.driver.find_element_by_xpath("//div[@class='tabs-container']/div/div/div[3]").get_attribute("id")
        print(card_id)

    def test_4_check_information(self):
        # check card icon
        self.assertIn("fa fa-cc-mastercard card-icon",
                      self.driver.find_element_by_xpath(
                          ".//*[@id='" + card_id + "']/div[1]/i").get_attribute("class"))

        # check card number
        self.assertIn("XXXX XXXX XXXX 4444",
                      self.driver.find_element_by_xpath(
                          ".//*[@id='" + card_id + "']/div[1]/span").get_attribute("textContent"))

        # check card date
        self.assertIn("\n                                05/2020                            ",
                      self.driver.find_element_by_xpath(
                          ".//*[@id='" + card_id + "']/div[2]").get_attribute("textContent"))

        # check card status
        self.assertIn("\n                                Active                            ",
                      self.driver.find_element_by_xpath(
                          ".//*[@id='" + card_id + "']/div[3]").get_attribute("textContent"))

    def test_5_make_primary(self):
        primary_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                ".//*[@id='" + card_id + "']/div[4]/i[3]")))
        primary_button.click()
        time.sleep(3)
        self.assertIn(card_id, self.driver.find_element_by_xpath("//div[@class='tabs-container']/div/div/div[2]").get_attribute("id"))

        primary_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                ".//*[@id='settings-row-1300016700']/div[4]/i[3]")))
        primary_button.click()
        time.sleep(5)
        self.assertIn(card_id, self.driver.find_element_by_xpath("//div[@class='tabs-container']/div/div/div[3]").get_attribute("id"))

    def test_6_delete_card(self):
        delete_card_button = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='" + card_id + "']/div[4]/i[2]")))
        delete_card_button.click()

        #delete
        WebDriverWait(self.driver, 3).until(EC.alert_is_present(), "Do you really want to perform this action?")
        alert = self.driver.switch_to_alert()
        alert.accept()

    def test_7_invoices_page(self):
        # go to invoices page
        invoice_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                               ".//*[@id='container']/div/div[2]/ul/li[2]/ul/div/div/li[7]/a")))
        invoice_button.click()
        self.assertIn("https://sandbox.opendrive.com/billing/invoices", self.driver.current_url)

        self.assertIn("Invoices",
                      self.driver.find_element_by_xpath(".//*[@id='container']/div/div[3]/h2/a").get_attribute("text"))

        # Invoices button in sidebar is active
        self.assertIn("item active billing-invoices",
                      self.driver.find_element_by_xpath(
                          ".//*[@id='container']/div/div[2]/ul/li[2]/ul/div/div/li[7]").get_attribute("class"))

        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div/div/div").is_displayed())

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == '__main__':
        unittest.main(verbosity=2)