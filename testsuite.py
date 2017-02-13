import unittest
from check_landing_page import check_landing_page
from login import login
from registration import registration
from open_folder import open_folder
from create_files import create_files
from delete_folder import delete_folder
from create_note import create_note
from task_create_delete import task_create_delete
from file_properties import file_properties
from task_edit import task_edit
from task_comment import task_comment
from create_delete_user import create_delete_edit_user
from settings import settings_change
from settings_2 import settings_change_2
from settings_3 import settings_change_3
from open_file import open_file
from admin_all_pages_check import admin_all_pages_check
from admin_users_page import admin_users_page
from admin_users_page_ney_payment import admin_new_payment


# get all tests
login_tests = unittest.TestLoader().loadTestsFromTestCase(login)
landing_page_tests = unittest.TestLoader().loadTestsFromTestCase(check_landing_page)
registration_test = unittest.TestLoader().loadTestsFromTestCase(registration)
open_folder_test = unittest.TestLoader().loadTestsFromTestCase(open_folder)
delete_folder_test = unittest.TestLoader().loadTestsFromTestCase(delete_folder)
create_files_test = unittest.TestLoader().loadTestsFromTestCase(create_files)
create_note_test = unittest.TestLoader().loadTestsFromTestCase(create_note)
task_create_delete_test = unittest.TestLoader().loadTestsFromTestCase(task_create_delete)
task_edit_test = unittest.TestLoader().loadTestsFromTestCase(task_edit)
task_comment_test = unittest.TestLoader().loadTestsFromTestCase(task_comment)
create_delete_users_test = unittest.TestLoader().loadTestsFromTestCase(create_delete_edit_user)
file_properties_test = unittest.TestLoader().loadTestsFromTestCase(file_properties)
settings_change_test = unittest.TestLoader().loadTestsFromTestCase(settings_change)
settings_change_2_test = unittest.TestLoader().loadTestsFromTestCase(settings_change_2)
settings_change_3_test = unittest.TestLoader().loadTestsFromTestCase(settings_change_3)
open_file_test = unittest.TestLoader().loadTestsFromTestCase(open_file)
admin_check_pages_test = unittest.TestLoader().loadTestsFromTestCase(admin_all_pages_check)
admin_users_page_test = unittest.TestLoader().loadTestsFromTestCase(admin_users_page)
admin_create_new_payment_test = unittest.TestLoader().loadTestsFromTestCase(admin_new_payment)

smoke_tests = unittest.TestSuite((login_tests, landing_page_tests, registration_test, open_folder_test,
                                  create_files_test, delete_folder_test, create_note_test,
task_create_delete_test, task_edit_test, task_comment_test, create_delete_users_test, file_properties_test,
settings_change_test, settings_change_2_test, settings_change_3_test, open_file_test,
                                  admin_check_pages_test, admin_users_page_test, admin_create_new_payment_test))

# run the suite
a = unittest.TextTestRunner(verbosity=2).run(smoke_tests)


