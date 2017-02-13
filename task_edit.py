import unittest, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

fake = Faker()
from selenium.webdriver.common.action_chains import ActionChains


class task_edit(unittest.TestCase):
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
        time.sleep(3)
        assert "https://sandbox.opendrive.com/tasks" in self.driver.current_url

    def test_2_create(self):
        # create project list
        create_prlist_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".fa.fa-plus.js-new-project-list.root-plus-btn")))
        create_prlist_button.click()
        project_list_name_field = self.driver.find_element_by_css_selector(
            ".project-list-name.js-project-list-name.with-placeholder.editing-item")
        pr_list_name = fake.company()
        project_list_name_field.send_keys(pr_list_name)
        project_list_name_field.send_keys(Keys.RETURN)
        time.sleep(3)
        self.assertEqual(pr_list_name, self.driver.find_element_by_xpath(
            ".//*[@id='container']/div/div[2]/ul/li[2]/ul/li[last()]/a[3]").get_attribute("title"))

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

    # create task list
        self.driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/ul/li[2]/ul/li/div/div/a").click()   #open project
        time.sleep(1)
        self.driver.find_element_by_css_selector(".br-btn.js-new-task-list-btn").click()                 #create task list
        task_list_name = self.driver.find_element_by_xpath("//*[@id='container']/div/div[5]/div/div/div[last()]/div/div[1]/table/tbody/tr/td[2]/div/span[1]")
        time.sleep(2)
        task_list_name.send_keys(fake.company())
        task_list_name.send_keys(Keys.RETURN)
        time.sleep(2)

    #create task
        self.driver.find_element_by_css_selector(".fa.fa-plus.btn-add-new-task.js-add-new-task").click()
        task_name_field = self.driver.find_element_by_css_selector(".js-task-name.with-placeholder.editing-item")
        task_name = fake.company()
        task_name_field.send_keys(task_name)
        task_name_field.send_keys(Keys.RETURN)
        self.assertEqual(task_name, self.driver.find_element_by_xpath(
            ".//*[@id='container']/div/div[5]/div/div/div/div[last()]/div[2]/table/tbody/tr/td[2]/div/div[1]/a").get_attribute(
            "text"))

    def test_3_edit_task(self):
        # edit task
        # edit progress
        self.driver.find_element_by_css_selector(".root-dir.root-dir-tasks").click()
        time.sleep(3)
        progress_button = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='container']/div/div[5]/div/div/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/div/div[2]/div/div/button")))
        progress_button.click()
        button_40 = wait.until(
            EC.element_to_be_clickable((By.XPATH, ".//*[@id='container']/div/div[5]/div/div/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/div/div[2]/div/div/div/ul/li[5]/a/span[1]" )))
        button_40.click()
        self.assertEqual("40%", progress_button.get_attribute("title"))

        #edit privacy
        privacy_button = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='container']/div/div[5]/div/div/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/div/div[2]/div/span/i")))
        self.assertEqual("This Task is Private", self.driver.find_element_by_xpath(
            ".//*[@id='container']/div/div[5]/div/div/div/div[2]/div[2]/table/tbody/tr/td[2]/div/div[2]/div/span/i").get_attribute("title"))
        privacy_button.click()
        time.sleep(3)
        self.assertEqual("This Task is Public", self.driver.find_element_by_xpath(
            ".//*[@id='container']/div/div[5]/div/div/div/div[2]/div[2]/table/tbody/tr/td[2]/div/div[2]/div/span/i").get_attribute("title"))

        #edit priority
        priority_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[2]")))
        priority_button.click()
        priority_medium = wait.until(
            EC.element_to_be_clickable((By.XPATH, ".//*[@id='container']/div/div[5]/div/div/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/div/div[2]/div/span/div/div/ul/li[3]/a/span[2]")))
        priority_medium.click()
        self.assertEqual("Priority: Medium", priority_button.get_attribute("title"))
        time.sleep(2)

        #edit task color
        find_task = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div/div[3]/div[2]/div[2]/table/tbody/tr/td[3]")
        color_button = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div/div[3]/div[2]/div[2]/table/tbody/tr/td[3]/a[2]")
        action = ActionChains(self.driver).move_to_element(find_task).move_to_element(color_button)
        time.sleep(2)
        action.click(color_button).perform()
        time.sleep(5)
        self.assertEqual("background-color: rgb(242, 222, 222); display: block;",
                         self.driver.find_element_by_xpath(
                             ".//*[@id='container']/div/div[5]/div/div/div[3]/div[2]").get_attribute("style"))

        #edit tag
        self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div/div[3]/div[2]/div[3]/div/button").click()
        self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div[1]/div[3]/div[2]/div[3]/div/div/ul/li[3]/a/span[1]").click()
        tag_button = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div[1]/div[3]/div[2]/div[3]/div/button")
        self.assertEqual("Fixed", tag_button.get_attribute("title"))
        time.sleep(2)

        #edit date
        self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div/div[3]/div[2]/div[4]/div/span[2]/span").click()
        self.driver.find_element_by_link_text("28").click()
        task_name = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/div/div[1]").get_attribute("title")

        #open task
        self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/div/div[1]").click()
        time.sleep(3)
        self.assertEqual("[1] " + task_name, self.driver.title)
        self.assertEqual("Fixed", (self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div[2]/div/div[2]/div[2]/div[3]/div[2]/button").get_attribute("title")))

        #edit tag
        tag_button = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div[2]/div/div[2]/div[2]/div[3]/div[2]/button")
        tag_button.click()
        self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/ul/li[5]/a/span[1]").click()
        time.sleep(1)
        self.assertEqual("In QA", tag_button.get_attribute("title"))

        #edit progress
        time.sleep(3)
        progress_button = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div[2]/div/div[1]/div[3]/div/div/button")
        progress_button.click()
        self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div[2]/div/div[1]/div[3]/div/div/div/ul/li[11]/a/span[1]").click()
        self.assertEqual("100%", progress_button.get_attribute("title"))

        #edit date
        date_button = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div[2]/div/div[2]/div[2]/div[2]/span[2]")
        date_button.click()
        self.driver.find_element_by_link_text("15").click()
        time.sleep(1)

    def test_4_delete(self):
        #delete project list
        find_project_list = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[2]/ul/li[2]/ul/li/a[3]")
        menu = self.driver.find_element_by_css_selector(".fa.fa-bars.js-item-menu-btn.dropdown-toggle")
        delete_button = self.driver.find_element_by_css_selector(".js-trash-project-list.orange-text")
        ActionChains(self.driver).move_to_element(find_project_list).move_to_element(menu).click(menu).perform()
        time.sleep(1)
        delete_button.click()

        # delete
        WebDriverWait(self.driver, 3).until(EC.alert_is_present(), "Do you really want to perform this action?")
        alert = self.driver.switch_to_alert()
        alert.accept()
        time.sleep(3)

        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    if __name__ == '__main__':
        unittest.main(verbosity=2)