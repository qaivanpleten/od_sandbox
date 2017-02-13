import unittest, time, random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from faker import Faker
fake = Faker()

class admin_users_page(unittest.TestCase):
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

    def test_3_select_user_type(self):
        x = 1
        while x < 7:
            select = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/h2/ul/li")
            all = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/h2/ul/li/ul/li[" + str(x) + "]")
            ActionChains(self.driver).move_to_element(select).click().move_to_element(all).click().perform()

            time.sleep(6)

            # check url
            # all
            if x == 1:
                self.assertIn(
                "https://sandbox.opendrive.com/admin/users?items_on_page=25&page=1&user_type=all&due_filter=&suspended=&search=&order_by=",
                self.driver.current_url)

            # free
            elif x == 2:
                self.assertIn("https://sandbox.opendrive.com/admin/users?items_on_page=25&page=1&user_type=free&due_filter=&suspended=&search=&order_by=",
                           self.driver.current_url)
            #premium
            elif x == 3:
                self.assertIn("https://sandbox.opendrive.com/admin/users?items_on_page=25&page=1&user_type=premium&due_filter=&suspended=&search=&order_by=",
                           self.driver.current_url)

            # suspended
            elif x == 4:
                self.assertIn(
                    "https://sandbox.opendrive.com/admin/users?items_on_page=25&page=1&user_type=suspended&due_filter=&suspended=&search=&order_by=",
                    self.driver.current_url)

            # closed
            elif x == 5:
                self.assertIn(
                    "https://sandbox.opendrive.com/admin/users?items_on_page=25&page=1&user_type=closed&due_filter=&suspended=&search=&order_by=",
                    self.driver.current_url)

            # trial
            elif x == 6:
                self.assertIn(
                    "https://sandbox.opendrive.com/admin/users?items_on_page=25&page=1&user_type=trials&due_filter=&suspended=&search=&order_by=",
                    self.driver.current_url)

            x += 1

    def test_4_items_on_page(self):
        select = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/h2/ul/li")
        all = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/h2/ul/li/ul/li[1]")
        ActionChains(self.driver).move_to_element(select).click().move_to_element(all).click().perform()
        time.sleep(4)

        # change items on page
        x = 1
        while x < 6:
            item_select = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div/div/div[1]/ul/li")
            item_number = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div/div/div[1]/ul/li/ul/li[" + str(x) + "]/a")
            ActionChains(self.driver).move_to_element(item_select).move_to_element(item_number).click().perform()
            #time.sleep(20)

            # check url
            # 10 items
            if x == 1:
                time.sleep(4)
                self.assertIn(
                    "https://sandbox.opendrive.com/admin/users?items_on_page=10&page=1&user_type=all&due_filter=&suspended=&search=&order_by=",
                    self.driver.current_url)

            # 25 items
            elif x == 2:
                time.sleep(4)
                self.assertIn(
                    "https://sandbox.opendrive.com/admin/users?items_on_page=25&page=1&user_type=all&due_filter=&suspended=&search=&order_by=",
                    self.driver.current_url)

            # 50 items
            elif x == 3:
                time.sleep(6)
                self.assertIn(
                    "https://sandbox.opendrive.com/admin/users?items_on_page=50&page=1&user_type=all&due_filter=&suspended=&search=&order_by=",
                    self.driver.current_url)

            # 100 items
            elif x == 4:
                time.sleep(15)
                self.assertIn(
                    "https://sandbox.opendrive.com/admin/users?items_on_page=100&page=1&user_type=all&due_filter=&suspended=&search=&order_by=",
                    self.driver.current_url)

            # 1000 items
            elif x == 5:
                time.sleep(30)
                self.assertIn(
                    "https://sandbox.opendrive.com/admin/users?items_on_page=1000&page=1&user_type=all&due_filter=&suspended=&search=&order_by=",
                    self.driver.current_url)

            x += 1

    def test_5_check_search(self):
        item_select = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[5]/div/div/div/div[1]/ul/li")
        item_number = self.driver.find_element_by_xpath(
            ".//*[@id='container']/div/div[5]/div/div/div/div[1]/ul/li/ul/li[1]/a")
        ActionChains(self.driver).move_to_element(item_select).move_to_element(item_number).click().perform()

        select = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/h2/ul/li")
        all = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div/h2/ul/li/ul/li[1]")
        ActionChains(self.driver).move_to_element(select).click().move_to_element(all).click().perform()

        time.sleep(4)

        # search
        search_input = self.driver.find_element_by_xpath(".//*[@id='container']/div/div[3]/div/input")
        search_input.clear()
        search_input.send_keys("qa.ivanpleten+1250")
        self.driver.find_element_by_xpath(".//*[@id='container']/div/div[3]/div/i").click()
        time.sleep(2)

        #check result
        self.assertIn("1724128", self.driver.find_element_by_xpath(
            ".//*[@id='container']/div/div[5]/div/div/div/div[2]/div[2]").get_attribute("data-userid"))

    def test_6_check_user_page(self):
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

    def test_7_edit_user_details(self):
        # change user details
        # change first name
        first_name_field = self.driver.find_element_by_id("admin-user-first-name")
        first_name_field.clear()
        fake_name = (fake.name().split(" "))[0]
        first_name_field.send_keys(fake_name)
        self.driver.find_element_by_id("save-admin-user-btn").click()
        time.sleep(2)
        self.assertIn(fake_name, self.driver.find_element_by_id("admin-user-first-name").get_attribute("value"))

        # change last name
        last_name_field = self.driver.find_element_by_id("admin-user-last-name")
        last_name_field.clear()
        fake_name = (fake.name().split(" "))[0]
        last_name_field.send_keys(fake_name)
        self.driver.find_element_by_id("save-admin-user-btn").click()
        time.sleep(2)
        self.assertIn(fake_name, self.driver.find_element_by_id("admin-user-last-name").get_attribute("value"))

        # change company name
        company_name_field = self.driver.find_element_by_id("admin-user-company")
        company_name_field.clear()
        fake_name = (fake.name().split(" "))[0]
        company_name_field.send_keys(fake_name)
        self.driver.find_element_by_id("save-admin-user-btn").click()
        time.sleep(2)
        self.assertIn(fake_name, self.driver.find_element_by_id("admin-user-company").get_attribute("value"))

        # change phone
        phone_field = self.driver.find_element_by_id("admin-user-phone")
        phone_field.clear()
        phone = str(random.randrange(0, 1000000, 7))
        phone_field.send_keys(phone)
        self.driver.find_element_by_id("save-admin-user-btn").click()
        time.sleep(2)
        self.assertIn(phone, self.driver.find_element_by_id("admin-user-phone").get_attribute("value"))

        # change web link
        web_link_field = self.driver.find_element_by_id("admin-user-weblink")
        web_link_field.clear()
        fake_name = (fake.name().split(" "))[0]
        web_link_field.send_keys(fake_name)
        self.driver.find_element_by_id("save-admin-user-btn").click()
        time.sleep(2)
        self.assertIn(fake_name, self.driver.find_element_by_id("admin-user-weblink").get_attribute("value"))

        # change password
        user_pass_field = self.driver.find_element_by_id("admin-user-password")
        repeat_pass_field = self.driver.find_element_by_id("admin-user-repeat-password")
        password = str(random.randrange(0, 1000000, 7))
        user_pass_field.clear()
        user_pass_field.send_keys(password)
        repeat_pass_field.clear()
        repeat_pass_field.send_keys(password)
        self.driver.find_element_by_id("save-admin-user-btn").click()
        time.sleep(2)

    def test_8_edit_account_details(self):
        # account type change
        x = 1
        while x < 3:
            Select(self.driver.find_element_by_id("admin-user-account-type")).select_by_value(""+ str(x) +"")
            self.driver.find_element_by_id("save-admin-user-btn").click()
            time.sleep(4)

            self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='admin-user-account-type']/option["+ str(x) +"]")
                                .is_selected())

            x += 1


        #account type change
        list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "90", "94", "95"]
        for a in list:
            Select(self.driver.find_element_by_xpath(".//*[@id='admin-user-plan']")).select_by_value("" + a + "")
            self.driver.find_element_by_id("save-admin-user-btn").click()
            time.sleep(3)

            self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='admin-user-plan']/option[@value="+ a +"]")
                                 .is_selected())

        # change suspended
        suspended_yes = self.driver.find_element_by_id("admin-user-suspended-yes").click()
        self.driver.find_element_by_id("save-admin-user-btn").click()
        time.sleep(2)
        self.assertTrue(self.driver.find_element_by_id("admin-user-suspended-yes").is_selected())
        self.assertIn("suspended", self.driver.find_element_by_xpath(".//*[@id='admin-user-edit']/div/div[1]/div[3]/span").get_attribute("class"))
        self.assertIn("(Suspended 0 days)", self.driver.find_element_by_xpath(".//*[@id='admin-user-edit']/div/div[1]/div[3]/span").get_attribute("textContent"))


        suspended_no = self.driver.find_element_by_id("admin-user-suspended-no").click()
        self.driver.find_element_by_id("save-admin-user-btn").click()
        time.sleep(2)
        self.assertTrue(self.driver.find_element_by_id("admin-user-suspended-no").is_selected())
        #refresh page
        self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div[2]/div/i[2]").click()
        time.sleep(2)


        # change trial
        trial_yes = self.driver.find_element_by_id("admin-user-trial-yes").click()
        self.driver.find_element_by_id("save-admin-user-btn").click()
        time.sleep(3)
        self.assertTrue(self.driver.find_element_by_id("admin-user-trial-yes").is_selected())
        self.assertIn("trial", self.driver.find_element_by_xpath(".//*[@id='admin-user-edit']/div/div[1]/div[3]/span").get_attribute("class"))
        self.assertIn("(Trial)", self.driver.find_element_by_xpath(".//*[@id='admin-user-edit']/div/div[1]/div[3]/span").get_attribute("textContent"))

        trial_no = self.driver.find_element_by_id("admin-user-trial-no").click()
        self.assertTrue(self.driver.find_element_by_id("admin-user-trial-no").is_selected())
        self.driver.find_element_by_id("save-admin-user-btn").click()
        time.sleep(2)
        # refresh page
        self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div[2]/div/i[2]").click()
        time.sleep(2)

        # change space
        space_value = self.driver.find_element_by_id("admin-user-space")
        space_value.clear()
        space_value.send_keys("100")
        Select(self.driver.find_element_by_id("admin-user-space-unit")).select_by_value("MB")
        self.driver.find_element_by_id("save-admin-user-btn").click()
        self.assertIn("100", self.driver.find_element_by_id("admin-user-space").get_attribute("value"))
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='admin-user-space-unit']/option[@value='MB']")
                                  .is_selected())

        Select(self.driver.find_element_by_id("admin-user-space-unit")).select_by_value("GB")
        space_value = self.driver.find_element_by_id("admin-user-space")
        space_value.clear()
        space_value.send_keys("1")
        self.driver.find_element_by_id("save-admin-user-btn").click()
        self.assertIn("1", self.driver.find_element_by_id("admin-user-space").get_attribute("value"))
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='admin-user-space-unit']/option[@value='GB']")
                                  .is_selected())
        # refresh page
        self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div[2]/div/i[2]").click()
        time.sleep(2)

        # change Bandwidth
        bandwidth_value = self.driver.find_element_by_id("admin-user-bw")
        bandwidth_value.clear()
        bandwidth_value.send_keys("100")
        Select(self.driver.find_element_by_id("admin-user-bw-unit")).select_by_value("MB")
        self.driver.find_element_by_id("save-admin-user-btn").click()
        self.assertIn("100", self.driver.find_element_by_id("admin-user-bw").get_attribute("value"))
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='admin-user-bw-unit']/option[@value='MB']")
                                  .is_selected())

        Select(self.driver.find_element_by_id("admin-user-bw-unit")).select_by_value("GB")
        bandwidth_value = self.driver.find_element_by_id("admin-user-bw")
        bandwidth_value.clear()
        bandwidth_value.send_keys("1")
        self.driver.find_element_by_id("save-admin-user-btn").click()
        self.assertIn("1", self.driver.find_element_by_id("admin-user-bw").get_attribute("value"))
        self.assertTrue(self.driver.find_element_by_xpath(".//*[@id='admin-user-bw-unit']/option[@value='GB']")
                                  .is_selected())
        # refresh page
        self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div[2]/div/i[2]").click()
        time.sleep(2)

        # change number of accaunt users
        acc_user_input = self.driver.find_element_by_id("admin-user-account-users")
        acc_user_input.clear()
        user_value = str(random.randrange(0, 10, 1))
        acc_user_input.send_keys(user_value)
        self.driver.find_element_by_id("save-admin-user-btn").click()
        self.assertIn(user_value, self.driver.find_element_by_id("admin-user-account-users").get_attribute("value"))
        # refresh page
        self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div[2]/div/i[2]").click()
        time.sleep(2)

        # change billing date
        bil_date = self.driver.find_element_by_id("admin-user-billing-date_1724128")
        bil_date.click()
        month = self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/span[1]").get_attribute(
            "textContent")
        year = self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/span[2]").get_attribute(
            "textContent")

        while month != "June" or year != "2017":
            # start = wait.until(EC.element_to_be_clickable((By.ID, "activity_start_date")))
            # start.click()
            next_button = self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/a[2]")
            next_button.click()
            month = self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/span[1]").get_attribute("textContent")
            year = self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/div/div/span[2]").get_attribute("textContent")
            time.sleep(1)

        self.driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[4]/td[4]/a").click()
        self.driver.find_element_by_id("save-admin-user-btn").click()

        self.assertIn("Jun 21, 2017", self.driver.find_element_by_id("admin-user-billing-date_1724128").get_attribute("value"))
        # refresh page
        self.driver.find_element_by_xpath(".//*[@id='container']/div/div[4]/div[2]/div/i[2]").click()
        time.sleep(2)


        # reset billing date
        self.driver.find_element_by_xpath(".//*[@id='tab-profile-content']/form/div[2]/div[9]/div/div/div[2]/a").click()
        self.driver.find_element_by_id("save-admin-user-btn").click()
        self.assertIn("n/a", self.driver.find_element_by_id("admin-user-billing-date_1724128").get_attribute("value"))

    def test_9_1_check_account_users(self):
        # open users tab
        users_tab = self.driver.find_element_by_id("tab-users")
        users_tab.click()
        # check tab
        self.assertIn("js-userinfo-tab active", self.driver.find_element_by_id("tab-users").get_attribute("class"))
        # check account user's info
        self.assertIn("jack lastname", self.driver.find_element_by_xpath(".//*[@id='tab-users-content']/div/div[2]/div[1]/div[2]/h3")
                      .get_attribute("title"))

    def test_9_2_check_logs_tab(self):
        # open logs tab
        logs_tab = self.driver.find_element_by_id("tab-logs")
        logs_tab.click()
        # check tab
        self.assertIn("js-userinfo-tab active", self.driver.find_element_by_id("tab-logs").get_attribute("class"))
        time.sleep(3)
        # check account user's info
        self.assertIn("No log records found.",
                      self.driver.find_element_by_xpath(".//*[@id='account-users-logs']/div")
                      .get_attribute("textContent"))

    def test_9_3_check_credit_cards(self):
        # open CC tab
        cc_tab = self.driver.find_element_by_id("tab-credit-cards")
        cc_tab.click()
        time.sleep(3)
        # check tab
        self.assertIn("js-userinfo-tab active", self.driver.find_element_by_id("tab-credit-cards").get_attribute("class"))
        # check account user's info
        self.assertIn("No credit cards found",
                      self.driver.find_element_by_xpath(".//*[@id='tab-credit-cards-content']/div")
                      .get_attribute("textContent"))

    def test_9_4_check_transaction_tab(self):
        # open transaction tab
        transaction_tab = self.driver.find_element_by_id("tab-transactions")
        transaction_tab.click()
        time.sleep(3)
        # check tab
        self.assertIn("js-userinfo-tab active", self.driver.find_element_by_id("tab-transactions").get_attribute("class"))
        # # check account user's info
        # self.assertIn("InvoiceNo items found.",
        #               self.driver.find_element_by_xpath(".//*[@id='tab-transactions-content']/div/div")
        #               .get_attribute("textContent"))

    def test_9_5_check_notes_tab(self):
        # open notes tab
        notes_tab = self.driver.find_element_by_id("tab-notes")
        notes_tab.click()
        time.sleep(3)
        # check tab
        self.assertIn("js-userinfo-tab active", self.driver.find_element_by_id("tab-notes").get_attribute("class"))

        #create new note
        add_note_button = self.driver.find_element_by_id("admin-add-note-btn")
        add_note_button.click()
        text_area = self.driver.find_element_by_id("new_note_text")
        text_area.clear()
        text = fake.text()
        text_area.send_keys(text)
        self.driver.find_element_by_id("admin-save-note-btn").click()
        time.sleep(3)
        #check note text
        self.assertIn(text, self.driver.find_element_by_xpath(".//*[@id='account-users-notes']/div/div[2]/div[2]/div").
                      get_attribute("textContent"))

    def test_9_6_check_acc_history(self):
        # open transaction tab
        history_tab = self.driver.find_element_by_id("tab-plans-history")
        history_tab.click()
        time.sleep(3)
        # check tab
        self.assertIn("js-userinfo-tab active", self.driver.find_element_by_id("tab-plans-history").get_attribute("class"))


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


    if __name__ == '__main__':
        unittest.main(verbosity=2)