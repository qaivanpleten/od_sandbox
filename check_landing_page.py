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

class check_landing_page(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://www.sandbox.opendrive.com")                   #Open page and wait
        cls.driver.title
        global wait
        wait = WebDriverWait(cls.driver, 15)



    def test_search_invalid(self):
        self.assertIn("OpenDrive", self.driver.title)  # check page title in HTML
        self.driver.find_element_by_class_name("searchtop").click()          #find and clock for element
        elem = self.driver.find_element_by_name("s")                         #looking for element
        elem.send_keys("pycon")                                              #Input word pycon in fild
        elem.send_keys(Keys.RETURN)                                          #keystroke Enter
        assert "Unfortunately" in self.driver.page_source                    #check result

    def test_search_valid(self):
        self.assertIn("OpenDrive", self.driver.title)  # check page title in HTML
        self.driver.find_element_by_class_name("searchtop").click()            # find and clock for element
        elem = self.driver.find_element_by_name("s")                           # looking for element
        elem.send_keys("mac")                                                  # Input word pycon in fild
        elem.send_keys(Keys.RETURN)
        assert "Unfortunately" not in self.driver.page_source

    def test_navigation(self):
        self.assertIn("OpenDrive", self.driver.title)   #check page title in HTML

        personal_button = wait.until(EC.element_to_be_clickable((By.ID, "menu-item-475")))   # go to page Personal
        personal_button.click()
        self.assertIn("OpenDrive – OpenDrive Personal", self.driver.title)                   

        business_button = wait.until(EC.element_to_be_clickable((By.ID, "menu-item-474")))   # go to page Business
        business_button.click()
        self.assertIn("OpenDrive – OpenDrive Business", self.driver.title)                   # check page title in HTML

        partner_button = wait.until(EC.element_to_be_clickable((By.ID, "menu-item-1909")))   # go to page Partner
        partner_button.click()
        self.assertIn("OpenDrive – OpenDrive Partners", self.driver.title)                   # check page title in HTML

    def test_plan_free(self):
        self.assertIn("OpenDrive", self.driver.title)                                                                                         # check page title in HTML
        pricing_button = wait.until(EC.element_to_be_clickable((By.ID, "menu-item-472"))).click()                                             # go to page Pricing
        self.assertIn("OpenDrive – OpenDrive Pricing", self.driver.title)                                                                     # check page title in HTML

        # personal plans
        self.driver.find_element_by_css_selector("a.upgrade-btn.get-started > span").click()                                                  #free account
        self.assertIn("OpenDrive – OpenDrive Sign Up", self.driver.title)                                                                     # check page title in HTML
        price = wait.until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='content']/div[1]/div/div[1]/div[1]/div/h4[2]/strong")))
        self.assertEqual("Free", price.text)                                                                                                  #check pricing

    def test_plan_custom_acc(self):
        pricing_button = wait.until(EC.element_to_be_clickable((By.ID, "menu-item-472"))).click()
        self.assertIn("OpenDrive – OpenDrive Pricing", self.driver.title)
        self.driver.find_element_by_css_selector("a.upgrade-btn.dropdown > span").click()                                                     #custom account
        self.driver.find_element_by_css_selector("ul.dropdown-content > li").click()
        self.assertIn("OpenDrive – OpenDrive Sign Up", self.driver.title)                                                                     # check page title in HTML
        price = wait.until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='content']/div[1]/div/div[1]/div[1]/div/h4[2]/strong")))     # price per month
        self.assertEqual("$5", price.text)
        price = wait.until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='content']/div[1]/div/div[1]/div[1]/div/h4[3]/strong")))     # price per year
        self.assertEqual("$50", price.text)

    def test_plan_custom_free(self):
        pricing_button = wait.until(EC.element_to_be_clickable((By.ID, "menu-item-472"))).click()
        self.assertIn("OpenDrive – OpenDrive Pricing", self.driver.title)                                                                     # check page title in HTML. Page Pricing
        self.driver.find_element_by_css_selector("a.upgrade-btn.dropdown > i.fa.fa-caret-down").click()                                       # custom account trial
        self.driver.find_element_by_css_selector("li.js-start_trial").click()
        self.assertIn("OpenDrive – OpenDrive Sign Up", self.driver.title)                                                                     # check page title in HTML
        plan = wait.until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='content']/div[1]/div/div[1]/div[1]/div/h6[2]/b")))
        self.assertEqual("Free 7 Day Trial", plan.text)
        price = wait.until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='content']/div[1]/div/div[1]/div[1]/div/h4[2]/strong")))     # price per month
        self.assertEqual("$5", price.text)
        price = wait.until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='content']/div[1]/div/div[1]/div[1]/div/h4[3]/strong")))     # price per year
        self.assertEqual("$50", price.text)

    def test_plan_personal(self):
        pricing_button = wait.until(EC.element_to_be_clickable((By.ID, "menu-item-472"))).click()
        self.assertIn("OpenDrive – OpenDrive Pricing", self.driver.title)
        self.driver.find_element_by_xpath(".//*[@id='content']/div[1]/div/div[2]/div[1]/div[3]/div/div[2]/div[1]/div[2]/a").click()               # personal account
        self.driver.find_element_by_xpath(".//*[@id='content']/div[1]/div/div[2]/div[1]/div[3]/div/div[2]/div[1]/div[2]/a/ul/li[1]").click()
        self.assertIn("OpenDrive – OpenDrive Sign Up", self.driver.title)                                                                     # check page title in HTML
        price = wait.until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='content']/div[1]/div/div[1]/div[1]/div/h4[2]/strong")))     # price per month
        self.assertEqual("$9.95", price.text)
        price = wait.until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='content']/div[1]/div/div[1]/div[1]/div/h4[3]/strong")))     # price per year
        self.assertEqual("$99", price.text)

    def test_plan_personal_free(self):
        pricing_button = wait.until(EC.element_to_be_clickable((By.ID, "menu-item-472"))).click()
        self.assertIn("OpenDrive – OpenDrive Pricing", self.driver.title)                                                                     # check page title in HTML. Page Pricing
        self.driver.find_element_by_xpath(".//*[@id='content']/div[1]/div/div[2]/div[1]/div[3]/div/div[2]/div[1]/div[2]/a").click()               # personal account trial
        self.driver.find_element_by_xpath(".//*[@id='content']/div[1]/div/div[2]/div[1]/div[3]/div/div[2]/div[1]/div[2]/a/ul/li[2]").click()
        self.assertIn("OpenDrive – OpenDrive Sign Up", self.driver.title)                                                                     # check page title in HTML
        price = wait.until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='content']/div[1]/div/div[1]/div[1]/div/h6[2]/b")))
        self.assertEqual("Free 7 Day Trial", price.text)
        price = wait.until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='content']/div[1]/div/div[1]/div[1]/div/h4[2]/strong")))     # price per month
        self.assertEqual("$9.95", price.text)
        price = wait.until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='content']/div[1]/div/div[1]/div[1]/div/h4[3]/strong")))     # price per year
        self.assertEqual("$99", price.text)

    def test_plan_business_custom(self):
        # busines plan
        pricing_button = wait.until(EC.element_to_be_clickable((By.ID, "menu-item-472"))).click()
        self.assertIn("OpenDrive – OpenDrive Pricing", self.driver.title)                                                                     # check page title in HTML. Page Pricing
        self.driver.find_element_by_xpath(".//*[@id='content']/div[1]/div/div[1]/a[2]").click()
        self.driver.find_element_by_xpath(".//*[@id='content']/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[2]/a").click()               # custom account
        self.driver.find_element_by_xpath(".//*[@id='content']/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[2]/a/ul/li[1]").click()
        self.assertIn("OpenDrive – OpenDrive Sign Up", self.driver.title)                                                                     # check page title in HTML
        price = wait.until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='content']/div[1]/div/div[1]/div[1]/div/h4[2]/strong")))     # price per month
        self.assertEqual("$7", price.text)
        price = wait.until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='content']/div[1]/div/div[1]/div[1]/div/h4[3]/strong")))     # price per year
        self.assertEqual("$70", price.text)

    def test_plan_business_custom_free(self):
        pricing_button = wait.until(EC.element_to_be_clickable((By.ID, "menu-item-472"))).click()
        self.assertIn("OpenDrive – OpenDrive Pricing", self.driver.title)                                                                     # check page title in HTML. Page Pricing
        self.driver.find_element_by_xpath(".//*[@id='content']/div[1]/div/div[1]/a[2]").click()
        self.driver.find_element_by_xpath(".//*[@id='content']/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[2]/a").click()               # custom account trial
        self.driver.find_element_by_xpath(".//*[@id='content']/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[2]/a/ul/li[2]").click()
        self.assertIn("OpenDrive – OpenDrive Sign Up", self.driver.title)                                                                     # check page title in HTML
        price = wait.until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='content']/div[1]/div/div[1]/div[1]/div/h6[2]/b")))
        self.assertEqual("Free 14 Day Trial", price.text)
        price = wait.until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='content']/div[1]/div/div[1]/div[1]/div/h4[2]/strong")))     # price per month
        self.assertEqual("$7", price.text)
        price = wait.until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='content']/div[1]/div/div[1]/div[1]/div/h4[3]/strong")))     # price per year
        self.assertEqual("$70", price.text)

    def test_plan_business_acc(self):
        pricing_button = wait.until(EC.element_to_be_clickable((By.ID, "menu-item-472"))).click()
        self.assertIn("OpenDrive – OpenDrive Pricing", self.driver.title)                                                                     # check page title in HTML. Page Pricing
        self.driver.find_element_by_xpath(".//*[@id='content']/div[1]/div/div[1]/a[2]").click()
        self.driver.find_element_by_xpath(".//*[@id='content']/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[2]/a").click()               # busines account
        self.driver.find_element_by_xpath(".//*[@id='content']/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[2]/a/ul/li[1]").click()
        self.assertIn("OpenDrive – OpenDrive Sign Up", self.driver.title)                                                                     # check page title in HTML
        price = wait.until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='content']/div[1]/div/div[1]/div[1]/div/h4[2]/strong")))     # price per month
        self.assertEqual("$29.95", price.text)
        price = wait.until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='content']/div[1]/div/div[1]/div[1]/div/h4[3]/strong")))     # price per year
        self.assertEqual("$299", price.text)

    def test_plan_business_free(self):
        pricing_button = wait.until(EC.element_to_be_clickable((By.ID, "menu-item-472"))).click()
        self.assertIn("OpenDrive – OpenDrive Pricing", self.driver.title)                                                                     # check page title in HTML. Page Pricing
        self.driver.find_element_by_xpath(".//*[@id='content']/div[1]/div/div[1]/a[2]").click()
        self.driver.find_element_by_xpath(".//*[@id='content']/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[2]/a").click()               # busines account trial
        self.driver.find_element_by_xpath(".//*[@id='content']/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div[2]/a/ul/li[2]").click()
        self.assertIn("OpenDrive – OpenDrive Sign Up", self.driver.title)                                                                     # check page title in HTML
        price = wait.until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='content']/div[1]/div/div[1]/div[1]/div/h6[2]/b")))
        self.assertEqual("Free 14 Day Trial", price.text)
        price = wait.until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='content']/div[1]/div/div[1]/div[1]/div/h4[2]/strong")))     # price per month
        self.assertEqual("$29.95", price.text)
        price = wait.until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='content']/div[1]/div/div[1]/div[1]/div/h4[3]/strong")))     # price per year
        self.assertEqual("$299", price.text)

    def test_plan_enterprise(self):
        pricing_button = wait.until(EC.element_to_be_clickable((By.ID, "menu-item-472"))).click()
        self.assertIn("OpenDrive – OpenDrive Pricing", self.driver.title)                                                                     # check page title in HTML. Page Pricing
        self.driver.find_element_by_xpath(".//*[@id='content']/div[1]/div/div[1]/a[2]").click()
        self.driver.find_element_by_xpath(".//*[@id='content']/div[1]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[2]/a").click()               # enterprise account
        self.driver.find_element_by_xpath(".//*[@id='content']/div[1]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[2]/a/ul/li[1]").click()
        self.assertIn("OpenDrive – OpenDrive Sign Up", self.driver.title)                                                                     # check page title in HTML
        price = wait.until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='content']/div[1]/div/div[1]/div[1]/div/h4[2]/strong")))     # price per month
        self.assertEqual("$59.95", price.text)
        price = wait.until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='content']/div[1]/div/div[1]/div[1]/div/h4[3]/strong")))     # price per year
        self.assertEqual("$599", price.text)

    def test_plan_enterprise_free(self):
        pricing_button = wait.until(EC.element_to_be_clickable((By.ID, "menu-item-472"))).click()
        self.assertIn("OpenDrive – OpenDrive Pricing", self.driver.title)                                                                     # check page title in HTML. Page Pricing
        self.driver.find_element_by_xpath(".//*[@id='content']/div[1]/div/div[1]/a[2]").click()
        self.driver.find_element_by_xpath(".//*[@id='content']/div[1]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[2]/a").click()               # enterprise account trial
        self.driver.find_element_by_xpath(".//*[@id='content']/div[1]/div/div[2]/div[2]/div[3]/div/div[2]/div[1]/div[2]/a/ul/li[2]").click()
        self.assertIn("OpenDrive – OpenDrive Sign Up", self.driver.title)                                                                     # check page title in HTML
        price = wait.until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='content']/div[1]/div/div[1]/div[1]/div/h6[2]/b")))
        self.assertEqual("Free 14 Day Trial", price.text)
        price = wait.until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='content']/div[1]/div/div[1]/div[1]/div/h4[2]/strong")))     # price per month
        self.assertEqual("$59.95", price.text)
        price = wait.until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='content']/div[1]/div/div[1]/div[1]/div/h4[3]/strong")))     # price per year
        self.assertEqual("$599", price.text)

    def test_od_for_win(self):
        wait = WebDriverWait(self.driver, 15)
        self.assertIn("OpenDrive", self.driver.title)  #check page title in HTML
        app_button = wait.until(EC.element_to_be_clickable((By.ID, "menu-item-597")))
        od_for_win = self.driver.find_element_by_id("menu-item-672")
        ActionChains(self.driver).move_to_element(app_button).move_to_element(od_for_win).click(od_for_win).perform()
        self.assertIn("OpenDrive – OpenDrive for Windows", self.driver.title)   #check page title in HTML
        sub_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".animated.fadeInDown.delay2")))
        self.assertEqual("OpenDrive Windows Desktop Application", sub_title.text)  #check subtitle

    def test_od_for_mac(self):
        wait = WebDriverWait(self.driver, 15)
        self.assertIn("OpenDrive", self.driver.title)  #check page title in HTML
        app_button = wait.until(EC.element_to_be_clickable((By.ID, "menu-item-597")))
        od_for_mac = self.driver.find_element_by_id("menu-item-671")
        ActionChains(self.driver).move_to_element(app_button).move_to_element(od_for_mac).click(od_for_mac).perform()
        self.assertIn("OpenDrive – OpenDrive for Mac", self.driver.title) #check page title in HTML
        sub_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".animated.fadeInDown.delay2")))
        self.assertEqual("OpenDrive Mac Desktop Application", sub_title.text)  #check subtitle

    def test_od_for_android(self):
        wait = WebDriverWait(self.driver, 15)
        self.assertIn("OpenDrive", self.driver.title)   #check page title in HTML
        app_button = wait.until(EC.element_to_be_clickable((By.ID, "menu-item-597")))
        od_for_android = self.driver.find_element_by_id("menu-item-1791")
        ActionChains(self.driver).move_to_element(app_button).move_to_element(od_for_android).click(od_for_android).perform()
        self.assertIn("OpenDrive – OpenDrive for Android", self.driver.title)   #check page title in HTML
        sub_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".animated.fadeInDown.delay2")))
        self.assertEqual("OpenDrive Android Application", sub_title.text)  #check subtitle

    def test_od_for_iphone(self):
        wait = WebDriverWait(self.driver, 15)
        self.assertIn("OpenDrive", self.driver.title)   #check page title in HTML
        app_button = wait.until(EC.element_to_be_clickable((By.ID, "menu-item-597")))
        od_for_iphone = self.driver.find_element_by_id("menu-item-1776")
        ActionChains(self.driver).move_to_element(app_button).move_to_element(od_for_iphone).click(od_for_iphone).perform()
        self.assertIn("OpenDrive – OpenDrive for iPhone", self.driver.title)   #check page title in HTML
        sub_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".animated.fadeInDown.delay2")))
        self.assertEqual("OpenDrive iPhone Application", sub_title.text)  #check subtitle

    def test_od_webdav(self):
        wait = WebDriverWait(self.driver, 15)
        self.assertIn("OpenDrive", self.driver.title)   #check page title in HTML
        app_button = wait.until(EC.element_to_be_clickable((By.ID, "menu-item-597")))
        od_for_webdav = self.driver.find_element_by_id("menu-item-1903")
        ActionChains(self.driver).move_to_element(app_button).move_to_element(od_for_webdav).click(od_for_webdav).perform()
        self.assertIn("OpenDrive – OpenDrive WebDAV", self.driver.title)   #check page title in HTML
        sub_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".animated.fadeInDown.delay2")))
        self.assertEqual("OpenDrive WebDAV Support", sub_title.text)  #check subtitle

    def test_od_driver_api(self):
        wait = WebDriverWait(self.driver, 15)
        self.assertIn("OpenDrive", self.driver.title)   #check page title in HTML
        app_button = wait.until(EC.element_to_be_clickable((By.ID, "menu-item-597")))
        od_driver_api = self.driver.find_element_by_id("menu-item-1902")
        ActionChains(self.driver).move_to_element(app_button).move_to_element(od_driver_api).click(od_driver_api).perform()
        self.assertIn("OpenDrive – OpenDrive API", self.driver.title)   #check page title in HTML
        sub_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".animated.fadeInDown.delay2")))
        self.assertEqual("OpenDrive API for developers", sub_title.text)  #check subtitle

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == '__main__':
        unittest.main()


