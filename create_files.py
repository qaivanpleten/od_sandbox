import unittest, time
from selenium import webdriver
from basetestcase import BaseTestCase
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from faker import Faker
fake_folder_name = Faker()

class create_files(unittest.TestCase):
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

    def test_2_create_files_list(self):
        wait = WebDriverWait(self.driver, 15)

        # list view
        list_view_button = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='container']/div[11]/div[3]/div/div/i[6]")))
        list_view_button.click()
        time.sleep(4)

        #create txt file
        find_container = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='container']/div[11]/div[3]/div/div/ul/li/i")))
        create_text = self.driver.find_element_by_id("new-file-txt")
        ActionChains(self.driver).move_to_element(find_container).move_to_element(create_text).click().perform()
        time.sleep(7)


        #create doc files
        find_container = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='container']/div[11]/div[3]/div/div/ul/li/i")))
        create_doc = self.driver.find_element_by_id("new-file-doc")
        ActionChains(self.driver).move_to_element(find_container).move_to_element(create_doc).click().perform()
        time.sleep(7)


        # create xls files
        find_container = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='container']/div[11]/div[3]/div/div/ul/li/i")))
        create_xls = self.driver.find_element_by_id("new-file-xls")
        ActionChains(self.driver).move_to_element(find_container).move_to_element(create_xls).click().perform()
        time.sleep(7)

        #check

        file_txt = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='tabs-container']/div/div/div[2]/div[3]/div[1]/div[1]/label")))
        self.assertEqual("Text.txt", file_txt.get_attribute("title"))

        file_doc = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='tabs-container']/div/div/div[2]/div[1]/div[1]/div[1]/label")))
        self.assertEqual("Document.doc", file_doc.get_attribute("title"))

        file_xls = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='tabs-container']/div/div/div[2]/div[2]/div[1]/div[1]/label")))
        self.assertEqual("Sheet.xls", file_xls.get_attribute("title"))

        #select all files
        select_all = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='container']/div[11]/div[3]/div/div/i[3]")))
        select_all.click()
        time.sleep(3)

        #delete
        delete_button = wait.until(EC.element_to_be_clickable((By.ID, "menu-trash-btn")))
        delete_button.click()
        time.sleep(5)

        WebDriverWait(self.driver, 3).until(EC.alert_is_present(), "Do you really want to perform this action?")
        alert = self.driver.switch_to_alert()
        alert.accept()
        time.sleep(7)
        self.driver.refresh()

    def test_3_create_files_grid(self):
        wait = WebDriverWait(self.driver, 15)
        grid_button = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='container']/div[11]/div[3]/div/div/i[5]")))
        grid_button.click()
        time.sleep(5)

        # create txt file
        find_container = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='container']/div[11]/div[3]/div/div/ul/li/i")))
        create_text = self.driver.find_element_by_id("new-file-txt")
        ActionChains(self.driver).move_to_element(find_container).move_to_element(create_text).click().perform()
        time.sleep(7)


        # create doc files
        find_container = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='container']/div[11]/div[3]/div/div/ul/li/i")))
        create_doc = self.driver.find_element_by_id("new-file-doc")
        ActionChains(self.driver).move_to_element(find_container).move_to_element(create_doc).click().perform()
        time.sleep(7)


        # create xls files
        find_container = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='container']/div[11]/div[3]/div/div/ul/li/i")))
        create_xls = self.driver.find_element_by_id("new-file-xls")
        ActionChains(self.driver).move_to_element(find_container).move_to_element(create_xls).click().perform()
        time.sleep(7)


        #check
        file_txt = wait.until(EC.element_to_be_clickable((By.XPATH, ".//div[@class='tabs-container']/div/div/div/div[3]/label")))
        self.assertEqual("Text.txt", file_txt.get_attribute("title"))

        file_doc = wait.until(EC.element_to_be_clickable((By.XPATH, ".//div[@class='tabs-container']/div/div/div/div[1]/label")))
        self.assertEqual("Document.doc", file_doc.get_attribute("title"))

        file_xls = wait.until(EC.element_to_be_clickable((By.XPATH, ".//div[@class='tabs-container']/div/div/div/div[2]/label")))
        self.assertEqual("Sheet.xls", file_xls.get_attribute("title"))

        # # create presentation
        # find_container = wait.until(
        #     EC.element_to_be_clickable((By.XPATH, "//*[@id='container']/div[11]/div[3]/div/div/ul/li/i")))
        # create_ppt = self.driver.find_element_by_id("new-file-ppt")
        # ActionChains(self.driver).move_to_element(find_container).move_to_element(create_ppt).click().perform()
        # time.sleep(5)
        # file_ppt = wait.until(EC.element_to_be_clickable((By.XPATH, ".//div[@class='tabs-container']/div/div/div/div[2]/label")))
        # self.assertEqual("Presentation.ppt", file_ppt.get_attribute("title"))

        # select all files
        select_all = wait.until(
            EC.element_to_be_clickable((By.XPATH, ".//*[@id='container']/div[11]/div[3]/div/div/i[3]")))
        select_all.click()
        time.sleep(2)

        # delete
        delete_button = wait.until(EC.element_to_be_clickable((By.ID, "menu-trash-btn")))
        delete_button.click()
        time.sleep(5)

        WebDriverWait(self.driver, 3).until(EC.alert_is_present(), "Do you really want to perform this action?")
        alert = self.driver.switch_to_alert()
        alert.accept()
        time.sleep(7)
        self.driver.refresh()

    def test_4_files_menu(self):
        wait = WebDriverWait(self.driver, 15)

        #create txt file
        find_container = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='container']/div[11]/div[3]/div/div/ul/li/i")))
        create_text = self.driver.find_element_by_id("new-file-txt")
        ActionChains(self.driver).move_to_element(find_container).move_to_element(create_text).click().perform()
        time.sleep(7)

        #delete file
        file = self.driver.find_element_by_xpath(
            ".//div[@class='js-tab-content tab-content scrollable folder']/div/div/div")
        menu = self.driver.find_element_by_xpath(
            ".//div[@class='js-tab-content tab-content scrollable folder']/div/div/div/i[3]")

        action = ActionChains(self.driver).move_to_element(file).move_to_element(menu)
        time.sleep(3)
        action.click(menu).perform()
        time.sleep(3)
        delete_button = self.driver.find_element_by_xpath(
            ".//div[@class='js-tab-content tab-content scrollable folder']/div/div/div/ul/li[9]/a")
        delete_button.click()
        time.sleep(3)

        WebDriverWait(self.driver, 3).until(EC.alert_is_present(), "Do you really want to perform this action?")
        alert = self.driver.switch_to_alert()
        alert.accept()
        time.sleep(5)

        #empty trash
        empty_trash = wait.until(EC.element_to_be_clickable((By.ID, "trash-clear-btn")))
        empty_trash.click()

        WebDriverWait(self.driver, 3).until(EC.alert_is_present(), "Do you really want to perform this action?")
        alert = self.driver.switch_to_alert()
        alert.accept()
        time.sleep(4)

    def test_5_delete_file_list(self):
        wait = WebDriverWait(self.driver, 15)

        #create txt file
        find_container = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='container']/div[11]/div[3]/div/div/ul/li/i")))
        create_text = self.driver.find_element_by_id("new-file-txt")
        ActionChains(self.driver).move_to_element(find_container).move_to_element(create_text).click().perform()
        time.sleep(7)

        # list view
        list_view_button = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='container']/div[11]/div[3]/div/div/i[6]")))
        list_view_button.click()
        time.sleep(4)

        file_container = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='tabs-container']/div/div/div/div[1]/div[1]/div[1]")))
        #file_container_2 = self.driver.find_element_by_xpath("//div[@class='tabs-container']/div/div/div/div[1]/div[2]/div[2]")
        trash_button = self.driver.find_element_by_xpath("//div[@class='tabs-container']/div/div/div/div[1]/div[1]/div[2]/i[3]")
        ActionChains(self.driver).move_to_element(file_container).move_to_element(trash_button).click().perform()
        time.sleep(5)

        WebDriverWait(self.driver, 3).until(EC.alert_is_present(), "Do you really want to perform this action?")
        alert = self.driver.switch_to_alert()
        alert.accept()
        time.sleep(5)

    def test_6_copy_file(self):
        wait = WebDriverWait(self.driver, 15)

        #create folder
        i = 0
        while i < 2:
            create_folder_button = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='container']/div[11]/div[2]/ul/li[1]/a[2]")))
            create_folder_button.click()
            folder_name = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                    '//ul[@class="folders-in-root items-container js-root-menu-items ps-container ps-theme-od"]/li[last()]/a/span')))
            folder_name.send_keys(fake_folder_name.company())
            folder_name.send_keys(Keys.RETURN)
            time.sleep(5)
            i += 1

        # list view
        list_view_button = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='container']/div[11]/div[3]/div/div/i[6]")))
        list_view_button.click()
        #self.driver.refresh()
        time.sleep(2)

        #open first folder
        open_f = wait.until(EC.element_to_be_clickable((By.XPATH,
                "//div[@class='tabs-container']/div/div/div/div[1]/div[@class='col-md-7 col-sm-7 filename-col']/a[@class='folder-thumb fa fa-folder']")))
        open_f.click()
        time.sleep(4)

        # create doc files
        find_container = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='container']/div[11]/div[3]/div/div/ul/li/i")))
        create_doc = self.driver.find_element_by_id("new-file-doc")
        ActionChains(self.driver).move_to_element(find_container).move_to_element(create_doc).click().perform()
        time.sleep(7)
        file_doc = wait.until(EC.element_to_be_clickable((By.XPATH, ".//div[@class='js-tab-content tab-content scrollable folder']/div/div/div/div[1]/label")))
        self.assertEqual("Document.doc", file_doc.get_attribute("title"))

        #move file
        file_container = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='tabs-container']/div/div/div/div[1]/div[1]/div[1]")))
        #file_container_2 = self.driver.find_element_by_xpath("//div[@class='tabs-container']/div/div/div/div[1]/div[2]/div[2]")
        menu = self.driver.find_element_by_xpath("//div[@class='tabs-container']/div/div/div/div[1]/div[1]/div[2]/i[4]")
        ActionChains(self.driver).move_to_element(file_container).move_to_element(menu).click().perform()
        move_button = self.driver.find_element_by_xpath(".//div[@class='js-tab-content tab-content scrollable folder']/div[2]/div/div[1]/ul/li[2]/a")
        move_button.click()


        #click to radiobutton in popup
        rd_button = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='file-folder-move']/div[2]/div[2]/div/div/li[3]/i[3]")))
        folder_id = self.driver.find_element_by_xpath(".//*[@id='file-folder-move']/div[2]/div[2]/div/div/li[3]").get_attribute("id")
        rd_button.click()
        #accept
        self.driver.find_element_by_id("move-file-folder-btn").click()
        time.sleep(5)


        #open second folder
        folder_second = wait.until(EC.element_to_be_clickable((By.ID, "folder-" + folder_id)))
        folder_second.click()
        time.sleep(5)
        #check file in folder
        container = self.driver.find_element_by_xpath("//*[@id='container']/div[11]/div[4]/div/div")
        self.assertEqual("folder-" + (folder_id), container.get_attribute("data-itemid"))

        # go to main folder
        icon = wait.until(
            EC.element_to_be_clickable((By.XPATH, ".//*[@id='container']/div[11]/div[2]/ul/li[1]/a[1]")))
        icon.click()
        time.sleep(5)

        # delete all files
        check_box = wait.until(
            EC.element_to_be_clickable((By.XPATH, ".//*[@id='container']/div[11]/div[3]/div/div/i[3]")))
        check_box.click()
        delete_button = wait.until(EC.element_to_be_clickable((By.ID, "menu-trash-btn")))
        delete_button.click()

        WebDriverWait(self.driver, 3).until(EC.alert_is_present(), "Do you really want to perform this action?")
        alert = self.driver.switch_to_alert()
        alert.accept()
        self.driver.delete_all_cookies()
        time.sleep(5)

    """def test_7_copy_file(self):
        wait = WebDriverWait(self.driver, 15)

        # grid view
        grid = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='container']/div[11]/div[3]/div/div/i[5]")))
        grid.click()
        time.sleep(3)

        #go to file page
        icon = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='container']/div[11]/div[2]/ul/li[1]/a[1]")))
        icon.click()
        time.sleep(5)
        self.assertEqual("MyDrive", (self.driver.find_element_by_xpath(".//*[@id='container']/header/div/div[2]/ul/li/a").get_attribute("title")))

        # select and delete all files and folders
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='container']/div[11]/div[3]/div/div/i[3]").click()

        # delete
        delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='menu-trash-btn']")))
        delete_button.click()
        time.sleep(3)

        WebDriverWait(self.driver, 3).until(EC.alert_is_present(), "Do you really want to perform this action?")
        alert = self.driver.switch_to_alert()
        alert.accept()
        time.sleep(3)
        self.driver.refresh()

        # create first new folder
        self.driver.get("http://www.sandbox.opendrive.com/files")
        self.driver.find_element_by_xpath('//div[@class="fill"]/div/ul/li/a[@title="Create Folder"]').click()
        folder_name = self.driver.find_element_by_xpath('//ul[@class="folders-in-root items-container js-root-menu-items ps-container ps-theme-od"]/li[last()]/a/span')
        fake_name = fake_folder_name.company()
        folder_name.send_keys(fake_name)
        folder_name.send_keys(Keys.RETURN)
        time.sleep(3)

        first_folder_id = (self.driver.find_element_by_xpath(".//ul[@class='root-menu js-root-menu']/li[2]/ul/li[1]").get_attribute("id"))
        print("the firsts folder id is " + first_folder_id)

        # create second new folder
        self.driver.get("http://www.sandbox.opendrive.com/files")
        self.driver.find_element_by_xpath('//div[@class="fill"]/div/ul/li/a[@title="Create Folder"]').click()
        folder_name = self.driver.find_element_by_xpath('//ul[@class="folders-in-root items-container js-root-menu-items ps-container ps-theme-od"]/li[last()]/a/span')
        fake_name = fake_folder_name.company()
        folder_name.send_keys(fake_name)
        folder_name.send_keys(Keys.RETURN)
        time.sleep(3)

        second_folder_id = (self.driver.find_element_by_xpath(".//ul[@class='root-menu js-root-menu']/li[2]/ul/li[2]").get_attribute("id"))
        print("the seconds folder id is " + second_folder_id)

        # open first folder
        self.driver.refresh()
        first_folder = wait.until(EC.element_to_be_clickable((By.XPATH, ".//div[@class='tabs-container']/div/div/div[2]/div[1]/div/a/i")))
        first_folder_id = self.driver.find_element_by_xpath(".//div[@class='tabs-container']/div/div/div[2]/div[1]").get_attribute("id")
        first_folder.click()
        self.assertEqual(first_folder_id, (self.driver.find_element_by_xpath(".//*[@id='container']/header/div/div[2]/ul/li").get_attribute("data-itemid")))
        time.sleep(5)

        # create doc files
        find_container = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='container']/div[11]/div[3]/div/div/ul/li/i")))
        create_doc = self.driver.find_element_by_xpath(".//*[@id='new-file-doc']")
        ActionChains(self.driver).move_to_element(find_container).move_to_element(create_doc).click().perform()
        time.sleep(4)
        file_id = self.driver.find_element_by_xpath(".//div[@class='tabs-container']/div/div/div[2]/div").get_attribute("id")
        print("file id is " + file_id)

        file_doc = wait.until(EC.element_to_be_clickable(
            (By.XPATH, ".//*[@id='" + file_id + "']/label")))
        self.assertEqual("Document.doc", file_doc.get_attribute("title"))

        # copy file
        file_container = wait.until(EC.element_to_be_clickable(
            (By.ID, file_id)))
        menu = self.driver.find_element_by_xpath(
            ".//*[@id='" + file_id + "']/div/a/i[3]")
        copy_button = self.driver.find_element_by_xpath(
            ".//*[@id='" + file_id + "']/div/ul/li[3]/a")
        ActionChains(self.driver).move_to_element(file_container).move_to_element(menu).click().move_to_element(copy_button).click().perform()
        time.sleep(10)

        # click radio button
        radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, ".//div[@class='move-copy-folders-list']/div/li[3]/i[3]")))
        radio_button.click()

        self.driver.find_element_by_xpath(".//*[@id='copy-file-folder-btn']").click()
        # refresh page and check the file
        self.driver.refresh()
        time.sleep(4)
        self.assertEqual("Document.doc", file_doc.get_attribute("title"))

        #go to second folder
        second_folder = wait.until(EC.element_to_be_clickable((By.XPATH, ".//div[@class='tabs-container']/div/div/div[2]/div[2]/div/a/i")))
        second_folder.click()
        file_doc = wait.until(EC.element_to_be_clickable(
            (By.XPATH, ".//*[@id='" + file_id + "']/label")))
        self.assertEqual("Document.doc", file_doc.get_attribute("title"))"""



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == '__main__':
        unittest.main(verbosity=2)

