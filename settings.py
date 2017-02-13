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

class settings_change(unittest.TestCase):
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

        # the presence of elements on the page
        a = 1
        while a < 5:
            cards_list = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div/div[" + str(a) + "]/div")
            self.assertTrue((cards_list).is_displayed())
            a += 1

        # check "files stats block"
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div/div[6]/div[1]").is_displayed())
        self.assertIn("Files Stats",
                      self.driver.find_element_by_xpath(
                          ".//*[@id='container']/div/div[4]/div/div/div[6]/div[1]/h3").get_attribute("textContent"))
        self.assertTrue(self.driver.find_element_by_id("filesChart").is_displayed())

        # check "Bandwidth Stats block"
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div/div[7]/div[1]").is_displayed())
        self.assertIn("Bandwidth Stats",
                      self.driver.find_element_by_xpath(
                          ".//*[@id='container']/div/div[4]/div/div/div[7]/div[1]/h3").get_attribute("textContent"))
        self.assertTrue(self.driver.find_element_by_id("bwChart").is_displayed())


    def test_2_go_to_my_profile(self):
        # go to My profile page
        my_profile_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                 ".//*[@id='container']/div/div[2]/ul/li[2]/ul/div/div/li[2]/a")))
        my_profile_button.click()
        self.assertIn("https://sandbox.opendrive.com/settings/profile", self.driver.current_url)
        self.assertIn("Profile", self.driver.find_element_by_xpath(".//*[@id='container']/div/div[3]/h2/a").get_attribute("text"))
        self.assertIn("item active settings-my-profile",
                      self.driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/ul/li[2]/ul/div/div/li[2]").get_attribute("class"))

    def test_3_first_name_change(self):
        self.assertIn("https://sandbox.opendrive.com/settings/profile", self.driver.current_url)
        fn_input = self.driver.find_element_by_id("user_info_first_name")
        fn_input.click()
        fn_input.clear()
        fake_first_name = fake.name()
        fake_first_name = fake_first_name.split(" ")
        fake_first_name = fake_first_name[0]
        print(fake_first_name)
        fn_input.send_keys(fake_first_name)
        fn_input.submit()
        time.sleep(2)
        self.assertIn(fake_first_name, self.driver.find_element_by_id("user_info_first_name").get_attribute("value"))

    def test_4_last_name_change(self):
        self.assertIn("https://sandbox.opendrive.com/settings/profile", self.driver.current_url)
        ln_input = self.driver.find_element_by_id("user_info_last_name")
        ln_input.click()
        ln_input.clear()
        fake_last_name = fake.name()
        fake_last_name = fake_last_name.split(" ")
        fake_last_name = fake_last_name[0]
        print(fake_last_name)
        ln_input.send_keys(fake_last_name)
        ln_input.submit()
        time.sleep(2)
        self.assertIn(fake_last_name, self.driver.find_element_by_id("user_info_last_name").get_attribute("value"))

    def test_5_company_change(self):
        self.assertIn("https://sandbox.opendrive.com/settings/profile", self.driver.current_url)
        comp_input = self.driver.find_element_by_id("user_info_company")
        comp_input.click()
        comp_input.clear()
        company_name = fake.company()
        print(company_name)
        comp_input.send_keys(company_name)
        comp_input.submit()
        time.sleep(2)
        self.assertIn(company_name, self.driver.find_element_by_id("user_info_company").get_attribute("value"))

    def test_6_time_zone(self):
        Select(self.driver.find_element_by_id("user_info_time_zone")).select_by_value("America/Montevideo")
        self.driver.find_element_by_xpath(".//*[@id='user-profile-form']/div/button").click()
        time.sleep(2)
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='user_info_time_zone']/option[31]").is_selected())

        Select(self.driver.find_element_by_id("user_info_time_zone")).select_by_value("Asia/Baghdad")
        self.driver.find_element_by_xpath(".//*[@id='user-profile-form']/div/button").click()
        time.sleep(2)
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='user_info_time_zone']/option[77]").is_selected())

    def test_7_file_versioning(self):
        Select(self.driver.find_element_by_id("user_info_versions")).select_by_value("5")
        self.driver.find_element_by_xpath(".//*[@id='user-profile-form']/div/button").click()
        time.sleep(2)
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='user_info_versions']/option[6]").is_selected())

        Select(self.driver.find_element_by_id("user_info_versions")).select_by_value("25")
        self.driver.find_element_by_xpath(".//*[@id='user-profile-form']/div/button").click()
        time.sleep(2)
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='user_info_versions']/option[26]").is_selected())

    def test_8_default_file_permissions(self):
        Select(self.driver.find_element_by_id("default_file_perm")).select_by_value("0")
        self.driver.find_element_by_xpath(".//*[@id='user-profile-form']/div/button").click()
        time.sleep(2)
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='default_file_perm']/option[1]").is_selected())

        Select(self.driver.find_element_by_id("default_file_perm")).select_by_value("2")
        self.driver.find_element_by_xpath(".//*[@id='user-profile-form']/div/button").click()
        time.sleep(2)
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='default_file_perm']/option[2]").is_selected())



    """def test_9_email_change(self):
        self.assertIn("https://sandbox.opendrive.com/settings/profile", self.driver.current_url)
        email_input = self.driver.find_element_by_id("user_info_email")
        email_input.click()
        email_input.clear()
        email = fake.name()
        email = email.split(" ")
        email = (email[0]) + "@gmail.com"
        print(email)
        email_input.send_keys(email)
        email_input.submit()
        time.sleep(2)
        self.assertIn("Email Address", self.driver.find_element_by_id("user_info_email").get_attribute("placeholder"))

        email_input.send_keys("qa.ivanpleten@gmail.com")
        email_input.submit()
        time.sleep(3)
        self.assertIn("qa.ivanpleten@gmail.com", self.driver.find_element_by_id("user_info_email").get_attribute("value"))
        """


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == '__main__':
        unittest.main(verbosity=2)