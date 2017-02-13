import unittest, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from faker import Faker

fake = Faker()
from selenium.webdriver.common.action_chains import ActionChains


class task_create_delete (unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://www.sandbox.opendrive.com/login")
        cls.driver.title
        global wait
        wait = WebDriverWait(cls.driver, 15)

    # login
    def test_1_login (self):
        username = self.driver.find_element_by_id("login_username")
        username.click()
        username.send_keys("qa.ivanpleten@gmail.com")
        password = self.driver.find_element_by_id("login_password")
        password.click()
        password.send_keys("rootpass")
        password.submit()
        assert "MyDrive" in self.driver.page_source
        assert "https://sandbox.opendrive.com/files" in self.driver.current_url

        self.driver.find_element_by_xpath(".//*[@id='container']/div[11]/div[1]/div/a[3]").click()
        assert "https://sandbox.opendrive.com/tasks" in self.driver.current_url

    def test_2_task_create_project(self):
        # create project list
        i = 0
        while i < 2:
            create_prlist_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".fa.fa-plus.js-new-project-list.root-plus-btn")))
            create_prlist_button.click()
            project_list_name_field = self.driver.find_element_by_css_selector(".project-list-name.js-project-list-name.with-placeholder.editing-item")
            pr_list_name = fake.company()
            project_list_name_field.send_keys(pr_list_name)
            project_list_name_field.send_keys(Keys.RETURN)
            time.sleep(2)
            self.assertEqual(pr_list_name, self.driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/ul/li[2]/ul/li[last()]/a[3]").get_attribute("title"))
            i += 1


    # create project
        find_project_list = self.driver.find_element_by_xpath("//*[@id='container']/div/div[2]/ul/li[2]/ul/li/a[3]")
        menu = self.driver.find_element_by_css_selector(".fa.fa-bars.js-item-menu-btn.dropdown-toggle")
        add_project = self.driver.find_element_by_css_selector(".js-add-project")
        action = ActionChains(self.driver).move_to_element(find_project_list).move_to_element(menu)
        time.sleep(1)
        action.click(menu).perform()
        add_project.click()
        time.sleep(1)

        # enter project name
        project_name_field = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/ul/li[2]/ul/li[1]/div/div[last()]/a")
        project_name = fake.company()
        project_name_field.send_keys(project_name)
        project_name_field.send_keys(Keys.RETURN)
        time.sleep(2)
        self.assertEqual(project_name, self.driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/ul/li[2]/ul/li[1]/div/div/a").get_attribute("text"))


    def test_3_create_tasks(self):
    # create task list
        self.driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/ul/li[2]/ul/li/div/div/a").click()
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='container']/div/div[3]/div[1]/a/i").click()
        time.sleep(2)
        task_list_name_field = self.driver.find_element_by_xpath("//*[@id='container']/div/div[5]/div/div/div[last()]/div/div[1]/table/tbody/tr/td[2]/div/span[1]")
        task_list_name = fake.company()
        task_list_name_field.send_keys(task_list_name)
        task_list_name_field.send_keys(Keys.RETURN)
        time.sleep(4)

    #create task
        i = 0
        while i < 2:
            self.driver.find_element_by_css_selector(".fa.fa-plus.btn-add-new-task.js-add-new-task").click()
            task_name_field = self.driver.find_element_by_css_selector(".js-task-name.with-placeholder.editing-item")
            task_name = fake.company()
            task_name_field.send_keys(task_name)
            task_name_field.send_keys(Keys.RETURN)
            i += 1
            self.assertEqual(task_name, self.driver.find_element_by_xpath(
                ".//*[@id='container']/div/div[5]/div/div/div/div[last()]/div[2]/table/tbody/tr/td[2]/div/div[1]/a").get_attribute(
                "text"))

    def test_4_delete_projectlists(self):
        # delete project list
        i = 0
        while i < 2:
            find_project_list = self.driver.find_element_by_xpath("//*[@id='container']/div/div[2]/ul/li[2]/ul/li/a[3]")
            menu = self.driver.find_element_by_css_selector(".fa.fa-bars.js-item-menu-btn.dropdown-toggle")
            delete_button = self.driver.find_element_by_css_selector(".js-trash-project-list.orange-text")
            action = ActionChains(self.driver).move_to_element(find_project_list).move_to_element(menu)
            time.sleep(2)
            action.click(menu).perform()
            time.sleep(2)
            delete_button.click()

        #delete
            WebDriverWait(self.driver, 3).until(EC.alert_is_present(), "Do you really want to perform this action?")
            alert = self.driver.switch_to_alert()
            alert.accept()
            time.sleep(4)
            i += 1

        self.driver.delete_all_cookies()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == '__main__':
        unittest.main(verbosity=2)