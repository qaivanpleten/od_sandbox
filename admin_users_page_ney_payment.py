import unittest, time, random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from faker import Faker
fake = Faker()

class admin_new_payment(unittest.TestCase):
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

    def test_2_check_users_page(self):
        # go to admin page
        admin_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".fa.fa-user-secret")))
        admin_button.click()
        self.assertIn("https://sandbox.opendrive.com/admin/users", self.driver.current_url)

        #check title in sidebar
        self.assertIn("Admin", self.driver.find_element_by_xpath(".//*[@id='container']/div/div[3]/ul/li[1]/a").get_attribute("textContent"))

        #check button in sidebar is active
        self.assertIn("item active", self.driver.find_element_by_xpath(".//*[@id='container']/div/div[3]/ul/li[2]/ul/li[1]").get_attribute("class"))

        # search
        search_input = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[3]/div/input")
        search_input.clear()
        search_input.send_keys("qa.ivanpleten+1250")
        self.driver.find_element_by_xpath(".//*[@id='container']/div/div[3]/div/i").click()
        time.sleep(2)

        # check result
        self.assertIn("1724128", self.driver.find_element_by_xpath(
            ".//*[@id='container']/div/div[5]/div/div/div/div[2]/div[2]").get_attribute("data-userid"))

        # find user and open it in new tab
        self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div/div/div[2]/div[2]/div[6]/i[2]").click()

        time.sleep(3)
        # check active tab
        self.assertIn("js-item-tab active tab-loaded", self.driver.find_element_by_xpath(
            ".//*[@id='container']/header/div/div[3]/ul/li[2]").get_attribute("class"))

        # check user id in tab
        self.assertIn("user-1724128",
                      self.driver.find_element_by_xpath(
                          ".//*[@id='container']/header/div/div[3]/ul/li[2]").get_attribute("data-itemid"))

    def test_3_check_payment_page(self):
        # go to payment page
        self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div[2]/div/i[1]").click()

    def test_4_create_payment(self):
        time.sleep(3)
        # select transaction date
        # select month
        a = random.randrange(1, 10, 1)
        x = 0
        while x < a:
            transaction_date_input = self.driver.find_element_by_id("payment_trans_date_1724128").click()
            next_button = self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/a[2]/span")
            next_button.click()
            x += 1

        # select day
        time.sleep(1)
        day = self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[3]/td[4]/a").click()

        #select  price_value
        price_value = self.driver.find_element_by_xpath(".//*[@id='new-payment-form']/div[3]/div[1]/div[3]/input")
        price_value.click()
        price_value.send_keys(10)

        # select transaction status
        y = str(random.randrange(0, 8, 1))
        trans_status = Select(self.driver.find_element_by_id("new_payment_trans_status")).select_by_index(y)

        trans_id_input = self.driver.find_element_by_xpath(".//*[@id='new-payment-form']/div[3]/div[3]/div[3]/input")
        trans_id = str(random.randrange(0, 10000000, 8))
        trans_id_input.send_keys(trans_id)

        # add note
        note_input = self.driver.find_element_by_id("new_payment_note")
        note = fake.text()
        note_input.send_keys(note)

        # select payment next date
        a = random.randrange(1, 10, 1)
        x = 0
        while x < a:
            transaction_date_input = self.driver.find_element_by_id("payment_due_date").click()
            next_button = self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/a[2]/span")
            next_button.click()
            x += 1

        # select day
        day = self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[3]/td[4]/a").click()

        # click submit button
        self.driver.find_element_by_xpath(".//*[@id='new-payment-form']/div[3]/div[5]/div[3]/a").click()


    def test_5_send_payment_reminder(self):
        menu_button = self.driver.find_element_by_xpath(".//*[@id='new-payment-form']/div[1]/div/div[1]")
        menu_button.click()
        send_reminder_button = self.driver.find_element_by_xpath(".//*[@id='new-payment-form']/div[1]/div/ul/li[1]/a")
        send_reminder_button.click()
        time.sleep(3)
        # check text
        self.assertIn("Payment remainder sent",
                      self.driver.find_element_by_xpath(".//*[@id='new-payment-form']/div[2]/div[3]/div/div/div[1]")
                      .get_attribute("title"))

    def test_6_trial_remainder_sent(self):
        menu_button = self.driver.find_element_by_xpath(".//*[@id='new-payment-form']/div[1]/div/div[1]")
        menu_button.click()
        send_reminder_button = self.driver.find_element_by_xpath(".//*[@id='new-payment-form']/div[1]/div/ul/li[2]/a")
        send_reminder_button.click()
        time.sleep(3)
        # check text
        self.assertIn("Trial remainder sent",
                      self.driver.find_element_by_xpath(".//*[@id='new-payment-form']/div[2]/div[3]/div/div/div[1]")
                      .get_attribute("title"))

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


    if __name__ == '__main__':
        unittest.main(verbosity=2)