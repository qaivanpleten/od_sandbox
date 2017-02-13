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


class task_comment(unittest.TestCase):
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
    def test_1_login(self):
        username = self.driver.find_element_by_id("login_username")
        username.click()
        username.send_keys("qa.ivanpleten@gmail.com")
        password = self.driver.find_element_by_id("login_password")
        password.click()
        password.send_keys("rootpass")
        password.submit()
        assert "MyDrive" in self.driver.page_source
        assert "https://sandbox.opendrive.com/files" in self.driver.current_url

        #go to tasks page
        task_page = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='container']/div[11]/div[1]/div/a[3]")))
        task_page.click()
        assert "https://sandbox.opendrive.com/tasks" in self.driver.current_url

    def test_2_create_project(self):
        # create project list
        create_prlist_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".fa.fa-plus.js-new-project-list.root-plus-btn")))
        create_prlist_button.click()
        project_list_name_field = self.driver.find_element_by_css_selector(
            ".project-list-name.js-project-list-name.with-placeholder.editing-item")
        pr_list_name = fake.company()
        project_list_name_field.send_keys(pr_list_name)
        project_list_name_field.send_keys(Keys.RETURN)
        time.sleep(2)
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
        project_name_field = self.driver.find_element_by_xpath(
            ".//*[@id='container']/div/div[2]/ul/li[2]/ul/li[1]/div/div[last()]/a")
        project_name = fake.company()
        project_name_field.send_keys(project_name)
        project_name_field.send_keys(Keys.RETURN)
        time.sleep(2)
        self.assertEqual(project_name, self.driver.find_element_by_xpath(
            ".//*[@id='container']/div/div[2]/ul/li[2]/ul/li[1]/div/div/a").get_attribute("text"))

        # create task list
        self.driver.find_element_by_xpath(
            ".//*[@id='container']/div/div[2]/ul/li[2]/ul/li/div/div/a").click()  # open project
        time.sleep(1)
        self.driver.find_element_by_css_selector(".br-btn.js-new-task-list-btn").click()  # create task list
        task_list_name = self.driver.find_element_by_xpath(
            "//*[@id='container']/div/div[5]/div/div/div[last()]/div/div[1]/table/tbody/tr/td[2]/div/span[1]")
        time.sleep(3)
        task_list_name.send_keys(fake.company())
        task_list_name.send_keys(Keys.RETURN)
        time.sleep(2)

        # create task
        self.driver.find_element_by_css_selector(".fa.fa-plus.btn-add-new-task.js-add-new-task").click()
        task_name_field = self.driver.find_element_by_css_selector(".js-task-name.with-placeholder.editing-item")
        global task_name
        task_name = fake.company()
        task_name_field.send_keys(task_name)
        task_name_field.send_keys(Keys.RETURN)
        self.assertEqual(task_name, self.driver.find_element_by_xpath(
            ".//*[@id='container']/div/div[5]/div/div/div/div[last()]/div[2]/table/tbody/tr/td[2]/div/div[1]/a").get_attribute(
            "text"))
        self.driver.find_element_by_css_selector(".root-dir.root-dir-tasks").click()
        time.sleep(5)

    def test_3_open_task(self):
        # open task
        # create description
        open_task = wait.until(
            EC.element_to_be_clickable((By.XPATH, ".//*[@id='container']/div/div[5]/div/div[1]/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/div/div[1]/a")))
        open_task.click()
        time.sleep(5)
        self.assertEqual(task_name, self.driver.find_element_by_xpath(".//*[@id='container']/div/div[3]/h2[2]/a[4]").get_attribute("title"))
        self.assertEqual("[1] " + task_name, self.driver.title)
        self.assertEqual("[1] " + task_name, self.driver.find_element_by_xpath(".//*[@id='container']/header/div/div[3]/ul/li[2]/a[1]").get_attribute("title"))

    def test_4_create_description(self):
        task_description_field = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='container']/div/div[5]/div/div[2]/div/div[3]/div/div[1]")))  # click on folder -> open folder
        task_deskription = fake.text()
        task_deskription = task_deskription[0:50]
        task_description_field.send_keys(task_deskription)
        self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div[2]/div/div[3]/div/div[2]/a[2]").click()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(3)
        self.assertEqual(task_deskription, self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div[2]/div/div[3]/div/div/div[1]/p").get_attribute("textContent"))

    def test_5_create_comment(self):

        # create comment
        i = 0
        while i < 5:
            comment_field = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div[2]/div/div[last()]/div[2]/div[1]")
            comment_field.click()
            time.sleep(2)
            comment = fake.text()
            comment = comment[0:50]
            comment_field.send_keys(comment)
            self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div[2]/div/div[last()]/div[2]/div[2]/a[2]").click()
            time.sleep(4)
            self.assertEqual(comment, self.driver.find_element_by_xpath(
                ".//*[@id='container']/div/div[5]/div/div[2]/div/div[last()-1]/div[2]/div[1]/div[1]/p").get_attribute("textContent"))
            i += 1


    def test_6_create_subcomment(self):
        # create subcomment
        i = 0
        while i < 5:
            find_task = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div[2]/div/div[4]/div[2]/div[1]/div[4]")
            subcomment_button = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div[2]/div/div[4]/div[2]/div[1]/div[4]/a[1]")
            action = ActionChains(self.driver).move_to_element(find_task).move_to_element(subcomment_button)
            time.sleep(2)
            action.click(subcomment_button).perform()
            time.sleep(3)
            subcomment_field = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='container']/div/div[5]/div/div[2]/div/div[4]/div[2]/div[2]/div[last()]/div[2]/div[1]")))
            subcomment = fake.text()
            subcomment = subcomment[0:50]
            subcomment_field.send_keys(subcomment)
            time.sleep(3)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, ".//*[@id='container']/div/div[5]/div/div[2]/div/div[4]/div[2]/div[2]/div[last()]/div[2]/div[2]/a[1]"))).click() #submit comment
            time.sleep(4)
            self.assertEqual(subcomment, self.driver.find_element_by_xpath(
                ".//*[@id='container']/div/div[5]/div/div[2]/div/div[4]/div[2]/div[2]/div[last()]/div[2]/div[1]/p").get_attribute("textContent"))
            i += 1


    def test_7_delete_subcomment(self):
        # delete subcomment
        find_subcomment = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div[2]/div/div[4]/div[2]/div[2]/div[1]/div[2]")
        delete_button = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div[2]/div/div[4]/div[2]/div[2]/div[1]/div[2]/div[3]/a[2]")
        action = ActionChains(self.driver).move_to_element(find_subcomment).move_to_element(delete_button)
        time.sleep(2)
        action.click(delete_button).perform()
        time.sleep(1)
        WebDriverWait(self.driver, 3).until(EC.alert_is_present(), "Do you really want to perform this action?")
        alert = self.driver.switch_to_alert()
        alert.accept()
        time.sleep(2)

    def test_8_delete_comment(self):
        # delete comment
        find_comment = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div[2]/div/div[4]/div[2]/div[1]")
        delete_button = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div[2]/div/div[4]/div[2]/div[1]/div[4]/a[3]")
        action = ActionChains(self.driver).move_to_element(find_comment).move_to_element(delete_button)
        time.sleep(3)
        action.click(delete_button).perform()
        time.sleep(3)
        WebDriverWait(self.driver, 3).until(EC.alert_is_present(), "Do you really want to perform this action?")
        alert = self.driver.switch_to_alert()
        alert.accept()
        time.sleep(3)

    def test_9_delete_project_list(self):
        #delete project list
        find_project_list = self.driver.find_element_by_xpath("//*[@id='container']/div/div[2]/ul/li[2]/ul/li/a[3]")
        menu = self.driver.find_element_by_css_selector(".fa.fa-bars.js-item-menu-btn.dropdown-toggle")
        delete_button = self.driver.find_element_by_css_selector(".js-trash-project-list.orange-text")
        ActionChains(self.driver).move_to_element(find_project_list).move_to_element(menu).click(menu).perform()
        time.sleep(1)
        delete_button.click()

        # delete
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