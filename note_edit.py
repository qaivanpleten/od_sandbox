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
        global wait
        wait = WebDriverWait(cls.driver, 15)


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
        # go to Notes page
        self.driver.find_element_by_xpath(".//*[@id='container']/div[11]/div[1]/div/a[2]").click()
        self.assertIn("https://sandbox.opendrive.com/notes", self.driver.current_url)

        # create Notepad
        self.driver.find_element_by_id("new-notpad-btn").click()
        notepad_name_input = self.driver.find_element_by_xpath("//ul[@class='root-menu js-root-menu']/li/ul/li[last()]/input")
        global notepad_name
        notepad_name = f.company()
        notepad_name_input.send_keys(notepad_name)
        notepad_name_input.send_keys(Keys.RETURN)
        self.driver.refresh()
        time.sleep(3)
        notepad = wait.until(EC.element_to_be_clickable((By.XPATH, ".//ul[@class='root-menu js-root-menu']/li[2]/ul/li/a")))
        self.assertEqual(notepad_name, notepad.get_attribute("title"))
        global notepad_id
        notepad_id = self.driver.find_element_by_xpath(".//ul[@class='root-menu js-root-menu']/li[2]/ul/li").get_attribute("id")


    def test_3_edit_note_color(self):
        # open notepad
        self.driver.find_element_by_id(notepad_id).click()
        self.assertEquals(notepad_name, self.driver.find_element_by_xpath(".//*[@id='container']/div/div[3]/h2/a").get_attribute("text"))

        #create first notation
        note_clear = self.driver.find_element_by_xpath(".//*[@id='ghost-notelist']/div/div/div/div[2]/div/div/div")
        note_clear.click()
        note_clear.send_keys(f.text())
        self.driver.find_element_by_xpath("//*[@id='container']/div/div[4]/div").click()
        time.sleep(3)

        #rename note
        self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div[2]/div/div/div/div[1]/div[2]/span").click()
        note_title = self.driver.find_element_by_xpath(".//*[@id='ghost-notelist']/div/div/div/div[1]/div[2]/input")
        note_title.click()
        global note_name
        note_name = f.company()
        note_title.clear()
        note_title.send_keys(note_name)
        note_title.send_keys(Keys.RETURN)
        time.sleep(3)
        self.driver.refresh()
        #check_color
        self.assertEqual("background-color: rgb(242, 242, 242);", self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div[2]/div/div/div").get_attribute("style"))

        #create second notation
        i = 0
        while i < 2:
            note = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='container']/div/div[4]/div/div[2]/div/div/div/div[1]")))
            add_notation_button = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div[2]/div/div/div/div[1]/div[2]/a[2]")
            ActionChains(self.driver).move_to_element(note).move_to_element(add_notation_button).click().perform()
            text_area = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div[2]/div/div/div/div[1]/div[2]/div[2]/textarea")
            text_area.send_keys(f.text())
            text_area.send_keys(Keys.RETURN)
            time.sleep(3)
            i += 1


        # change color of notelist and check
        a = 0
        while a < 5:
        # open menu
            self.driver.refresh()
            time.sleep(2)
            note = wait.until(
            EC.element_to_be_clickable((By.XPATH, ".//*[@id='container']/div/div[4]/div/div[2]/div/div/div/div[1]")))
            menu_button = self.driver.find_element_by_xpath(
                ".//*[@id='container']/div/div[4]/div/div[2]/div/div/div/div[1]/div[2]/a[1]")
            ActionChains(self.driver).move_to_element(note).move_to_element(menu_button).click().perform()
            # change color
            self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a[5]").click()
            a += 1
            time.sleep(2)

            # check
            if a == 1:
                # yellow
                self.assertEqual("background-color: rgb(250, 242, 147);", self.driver.find_element_by_xpath(
                    ".//*[@id='container']/div/div[4]/div/div[2]/div/div/div").get_attribute("style"))

            elif a == 2:
                # red
                self.assertEqual("background-color: rgb(250, 141, 131);", self.driver.find_element_by_xpath(
                    ".//*[@id='container']/div/div[4]/div/div[2]/div/div/div").get_attribute("style"))

            elif a == 3:
                # green
                self.assertEqual("background-color: rgb(202, 253, 143);", self.driver.find_element_by_xpath(
                    ".//*[@id='container']/div/div[4]/div/div[2]/div/div/div").get_attribute("style"))

            elif a == 4:
                # blue
                self.assertEqual("background-color: rgb(137, 207, 237);", self.driver.find_element_by_xpath(
                    ".//*[@id='container']/div/div[4]/div/div[2]/div/div/div").get_attribute("style"))

            elif a == 5:
                # gray
                self.assertEqual("background-color: rgb(242, 242, 242);", self.driver.find_element_by_xpath(
                    ".//*[@id='container']/div/div[4]/div/div[2]/div/div/div").get_attribute("style"))

    def test_4_change_size_of_note(self):
        a = 0
        while a < 3:
            # open menu
            self.driver.refresh()
            time.sleep(4)
            note = wait.until(
                EC.element_to_be_clickable((By.XPATH, ".//*[@id='container']/div/div[4]/div/div[2]/div/div/div/div[1]")))
            menu_button = self.driver.find_element_by_xpath(
                ".//*[@id='container']/div/div[4]/div/div[2]/div/div/div/div[1]/div[2]/a[1]")
            ActionChains(self.driver).move_to_element(note).move_to_element(menu_button).click().perform()
            time.sleep(1)
            # change size
            self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a[1]").click()
            a += 1
            time.sleep(3)

            #check
            #middle
            if a == 1:
                self.assertEqual("notelist-container col-md-6 col-sm-12", self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div[2]").get_attribute("class"))
                self.assertEqual("notelist-rect-h", self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div[2]/div ").get_attribute("class"))
            #big
            elif a == 2:
                self.assertEqual("notelist-container col-md-6 col-sm-12", self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div[2]").get_attribute("class"))
                self.assertEqual("notelist-square", self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div[2]/div ").get_attribute("class"))

            #little
            elif a == 3:
                self.assertEqual("notelist-container col-md-3 col-sm-6", self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div[2]").get_attribute("class"))
                self.assertEqual("notelist-square", self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div[2]/div ").get_attribute("class"))

    def test_5_check_in_notation(self):
        # check
        self.assertEqual("one-note drop-file ",
                         self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div[2]/div/div/div/div[2]/div/div[2]").get_attribute("class"))
        # click check_box
        self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div[2]/div/div/div/div[2]/div/div[2]/i[1]").click()
        time.sleep(2)
        # check
        self.assertEqual("one-note drop-file  checked",
                         self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div[2]/div/div/div/div[2]/div/div[2]").get_attribute("class"))

    def test_6_delete_notation(self):
        container = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='container']/div/div[4]/div/div[2]/div/div/div/div[2]/div/div[2]")))
        delete_button = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/a")
        ActionChains(self.driver).move_to_element(container).move_to_element(delete_button).click().perform()

        # accept delete
        WebDriverWait(self.driver, 3).until(EC.alert_is_present(), "Do you really want to perform this action?")
        alert = self.driver.switch_to_alert()
        alert.accept()
        time.sleep(5)

    def test_7_delete_note(self):
        self.driver.refresh()
        time.sleep(4)
        note = wait.until(
            EC.element_to_be_clickable((By.XPATH, ".//*[@id='container']/div/div[4]/div/div[2]/div/div/div/div[1]")))
        menu_button = self.driver.find_element_by_xpath(
            ".//*[@id='container']/div/div[4]/div/div[2]/div/div/div/div[1]/div[2]/a[1]")
        ActionChains(self.driver).move_to_element(note).move_to_element(menu_button).click().perform()
        # delete note
        self.driver.find_element_by_xpath(
            ".//*[@id='container']/div/div[4]/div/div[2]/div/div/div/div[1]/div[2]/div[1]/a[2]").click()
        time.sleep(1)

        # accept delete
        WebDriverWait(self.driver, 3).until(EC.alert_is_present(), "Do you really want to perform this action?")
        alert = self.driver.switch_to_alert()
        alert.accept()
        time.sleep(5)

    """def test_8_drag_and_drop(self):
        self.driver.refresh()
        time.sleep(4)
        # open notepad
        self.driver.find_element_by_id(notepad_id).click()
        self.assertEquals(notepad_name, self.driver.find_element_by_xpath(".//*[@id='container']/div/div[3]/h2/a").get_attribute("text"))

        #create first notation
        note_clear = self.driver.find_element_by_xpath(".//*[@id='ghost-notelist']/div/div/div/div[2]/div/div/div")
        note_clear.click()
        note_clear.send_keys(f.text())
        self.driver.find_element_by_xpath("//*[@id='container']/div/div[4]/div").click()
        time.sleep(3)

        #create note
        i = 0
        while i < 8:
            new_note_button = self.driver.find_element_by_id("new-notelist-btn").click()
            time.sleep(3)
            note = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                          ".//*[@id='container']/div/div[4]/div/div[1]/div/div/div/div[2]/div/div[1]/div")))
            note.click()
            note.send_keys(f.text())
            self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]").click()
            time.sleep(3)
            i += 1"""

    def test_9_delete_notepad(self):
        # delete Notepad
        find_notepad = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='" + notepad_id + "']")))
        menu = self.driver.find_element_by_xpath("//div[@class='dirs js-left-sidebar notepads']/ul/li/ul/li[1]/i[1]")
        trash = self.driver.find_element_by_xpath(
            "//div[@class='dirs js-left-sidebar notepads']/ul/li/ul/li[1]/ul/li[3]")
        ActionChains(self.driver).move_to_element(find_notepad).move_to_element(menu).click().perform()
        trash.click()
        time.sleep(2)

        # accept delete
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