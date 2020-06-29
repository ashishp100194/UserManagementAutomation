from common import common
import variables

common=common()
def test_login_via_admin():
    common.login(variables.objectRepo['admin_user'],variables.objectRepo['admin_password'],admin=True)
    common.logout()

def test_create_user():
    common.login(variables.objectRepo['admin_user'],variables.objectRepo['admin_password'],admin=True)
    common.addUser()

def test_login_via_user():
    common.login(variables.objectRepo['user_1'],variables.objectRepo['password_1'])
    common.logout()

def test_search_user():
    common.login(variables.objectRepo['admin_user'],variables.objectRepo['admin_password'],admin=True)
    common.searchUser('admin')