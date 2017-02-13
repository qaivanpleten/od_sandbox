import unittest, time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from faker import Faker
f = Faker()

class create_note(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://www.sandbox.opendrive.com/login")                   #Open page and wait
        cls.driver.title

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

    def test_2_create_notepad(self):
        wait = WebDriverWait(self.driver, 15)
        # go to Notes page
        self.driver.find_element_by_xpath(".//*[@id='container']/div[11]/div[1]/div/a[2]").click()
        self.assertIn("https://sandbox.opendrive.com/notes", self.driver.current_url)

        # create Notepad
        self.driver.find_element_by_id("new-notpad-btn").click()
        notepad_name_input = self.driver.find_element_by_xpath("//ul[@class='root-menu js-root-menu']/li/ul/li[last()]/input")
        notepad_name = f.company()
        notepad_name_input.send_keys(notepad_name)
        notepad_name_input.send_keys(Keys.RETURN)
        self.driver.refresh()
        notepad = wait.until(EC.element_to_be_clickable((By.XPATH, ".//ul[@class='root-menu js-root-menu']/li[2]/ul/li/a")))
        self.assertEqual(notepad_name, notepad.get_attribute("title"))



        #open Notepad
        self.driver.find_element_by_xpath("//ul[@class='root-menu js-root-menu']/li/ul/li[last()]/a/span").click()

        # enter text
        note = self.driver.find_element_by_xpath(".//*[@id='ghost-notelist']/div/div/div/div[2]/div/div/div")
        note.send_keys(f.text())
        self.driver.find_element_by_xpath("//*[@id='container']/div/div[4]/div").click()

        # create note
        self.driver.find_element_by_xpath("//*[@id='new-notelist-btn']/i").click()
        note = self.driver.find_element_by_xpath("//*[@id='container']/div/div[4]/div/div[1]/div/div/div/div[2]/div/div[1]/div")
        note.send_keys(f.text())
        self.driver.find_element_by_xpath("//*[@id='container']/div/div[4]/div").click()

        #create one more note
        find_note = self.driver.find_element_by_xpath("//*[@id='container']/div/div[4]/div/div[3]/div/div/div/div[1]")
        create_button = self.driver.find_element_by_xpath("//*[@id='container']/div/div[4]/div/div[3]/div/div/div/div[1]/div[2]/a[2]")
        action = ActionChains(self.driver).move_to_element(find_note).move_to_element(create_button)

        action.click(create_button).perform()
        enter_text = self.driver.find_element_by_xpath("//*[@id='container']/div/div[4]/div/div[3]/div/div/div/div[1]/div[2]/div[2]/textarea")
        enter_text.send_keys(f.text())
        enter_text.send_keys(Keys.ENTER)
        # delete note

        find_note = self.driver.find_element_by_xpath("//*[@id='container']/div/div[4]/div/div[3]/div/div/div/div[1]")
        menu = self.driver.find_element_by_xpath("//*[@id='container']/div/div[4]/div/div[3]/div/div/div/div[1]/div[2]/a[1]")
        trash = self.driver.find_element_by_xpath("//*[@id='container']/div/div[4]/div/div[3]/div/div/div/div[1]/div[2]/div[1]/a[2]")
        action = ActionChains(self.driver).move_to_element(find_note).move_to_element(menu)
        action.click(menu).perform()
        action = ActionChains(self.driver).move_to_element(find_note).move_to_element(trash)
        action.click(trash).perform()

        #accept delete
        WebDriverWait(self.driver, 3).until(EC.alert_is_present(), "Do you really want to perform this action?")
        alert = self.driver.switch_to_alert()
        alert.accept()

        # delete Notepad
        find_notepad = self.driver.find_element_by_xpath("//div[@class='dirs js-left-sidebar notepads']/ul/li/ul/li[1]")
        menu = self.driver.find_element_by_xpath("//div[@class='dirs js-left-sidebar notepads']/ul/li/ul/li[1]/i[1]")
        trash = self.driver.find_element_by_xpath("//div[@class='dirs js-left-sidebar notepads']/ul/li/ul/li[1]/ul/li[3]")
        action = ActionChains(self.driver).move_to_element(find_notepad).move_to_element(menu)
        action.click(menu).perform()
        trash.click()
        time.sleep(2)

        #accept delete
        WebDriverWait(self.driver, 3).until(EC.alert_is_present(), "Do you really want to perform this action?")
        alert = self.driver.switch_to_alert()
        alert.accept()
        time.sleep(3)

        # empty trash
        self.driver.find_element_by_xpath(".//*[@id='trash-clear-btn']").click()
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