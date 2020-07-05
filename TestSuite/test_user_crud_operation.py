from common import common
import variables
import TestData

common=common()

def test_login_via_admin():
    common.login(variables.objectRepo['admin_user'],variables.objectRepo['admin_password'],admin=True)
    common.logout()

def test_verify_create_user():
    common.login(variables.objectRepo['admin_user'],variables.objectRepo['admin_password'],admin=True)
    common.addUser(TestData.new_user["User_Id"],TestData.new_user["Password"],TestData.new_user["First_Name"],TestData.new_user["Last_Name"])
    common.logout()

def test_verify_login_via_user():
    common.login(variables.objectRepo['admin_user'], variables.objectRepo['admin_password'], admin=True)
    common.addUser(TestData.new_user["User_Id"], TestData.new_user["Password"], TestData.new_user["First_Name"],TestData.new_user["Last_Name"])
    common.logout(quit=False)
    common.login(TestData.new_user["User_Id"],TestData.new_user["Password"],browser=False)
    common.logout()

def test_verify_update_first_name():
    common.login(variables.objectRepo['admin_user'], variables.objectRepo['admin_password'], admin=True)
    common.addUser(TestData.new_user["User_Id"], TestData.new_user["Password"], TestData.new_user["First_Name"],TestData.new_user["Last_Name"])
    common.logout(quit=False)
    common.login(TestData.new_user["User_Id"],TestData.new_user["Password"],browser=False)
    common.updateUserDetails('First_Name','Updated_First_Name')

def test_verify_update_last_name():
    common.login(variables.objectRepo['admin_user'], variables.objectRepo['admin_password'], admin=True)
    common.addUser(TestData.new_user["User_Id"], TestData.new_user["Password"], TestData.new_user["First_Name"],TestData.new_user["Last_Name"])
    common.logout(quit=False)
    common.login(TestData.new_user["User_Id"],TestData.new_user["Password"],browser=False)
    common.updateUserDetails('Last_Name','Updated_Last_Name')

def test_verify_update_password():
    common.login(variables.objectRepo['admin_user'], variables.objectRepo['admin_password'], admin=True)
    common.addUser(TestData.new_user["User_Id"], TestData.new_user["Password"], TestData.new_user["First_Name"],TestData.new_user["Last_Name"])
    common.logout(quit=False)
    common.login(TestData.new_user["User_Id"],TestData.new_user["Password"],browser=False)
    common.updateUserDetails('Password','Admin@123')

def test_verify_delete_user():
    common.login(variables.objectRepo['admin_user'], variables.objectRepo['admin_password'], admin=True)
    common.addUser(TestData.new_user["User_Id"], TestData.new_user["Password"], TestData.new_user["First_Name"],TestData.new_user["Last_Name"])
    common.deleteUser(TestData.new_user["User_Id"])

def test_verify_invalid_user():
    common.login(TestData.new_user["User_Id"],TestData.new_user["Password"],invalid=True)