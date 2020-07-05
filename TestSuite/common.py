from config import config
import variables
import time

class common(config):

    def __init__(self):
        self.driver=self.start_browser("chrome")


    def login(self,user_id,password,browser=True,remember_me=False,admin=False,invalid=False):
        if browser:
            self.driver.get(variables.objectRepo['url'])
        self.wait_for_locator(variables.locatorRepo['user_id'])
        self.driver.find_element_by_xpath(variables.locatorRepo['user_id']).send_keys(user_id)
        self.driver.find_element_by_xpath(variables.locatorRepo['password']).send_keys(password)
        if remember_me:
            self.driver.find_element_by_xpath(variables.locatorRepo['remember_me']).click()
        self.driver.find_element_by_xpath(variables.locatorRepo['submit_button']).click()
        if invalid:
            Invalid_Creds_Msg=self.driver.find_element_by_xpath(variables.locatorRepo['Invalid_Creds']).text
            assert (Invalid_Creds_Msg==variables.expectedValues['invalidCredsMsg'])
            exit()
        if admin:
            self.wait_for_locator(variables.locatorRepo['AddUser'])
            assert (" AddUser " in self.driver.page_source)
        else:
            self.wait_for_locator(variables.locatorRepo['MyProfile'])
            assert (" AddUser " not in self.driver.page_source)

    def logout(self,quit=True):
        self.wait_for_locator(variables.locatorRepo['SignOut'])
        self.driver.find_element_by_xpath(variables.locatorRepo['SignOut']).click()
        self.wait_for_locator(variables.locatorRepo['submit_button'])
        if quit:
            self.driver.close()

    def addUser(self,User_Id,Password,First_Name=None,Last_Name=None):
        self.driver.find_element_by_xpath(variables.locatorRepo['User_Id']).send_keys(User_Id)
        self.driver.find_element_by_xpath(variables.locatorRepo['Password']).send_keys(Password)
        if First_Name:
            self.driver.find_element_by_xpath(variables.locatorRepo['First_Name']).send_keys(First_Name)
        if Last_Name:
            self.driver.find_element_by_xpath(variables.locatorRepo['Last_Name']).send_keys(Last_Name)
        self.driver.find_element_by_xpath(variables.locatorRepo['submit_button']).click()

    def searchUser(self,User_Id):
        self.driver.find_element_by_xpath(variables.locatorRepo['ViewUsers']).click()
        self.driver.find_element_by_xpath(variables.locatorRepo['Search']).send_keys(User_Id)

    def updateUserDetails(self, field, expected_value):
        self.wait_for_locator(variables.locatorRepo[field])
        self.driver.find_element_by_xpath(variables.locatorRepo[field]).clear()
        self.driver.find_element_by_xpath(variables.locatorRepo[field]).send_keys(expected_value)
        self.driver.find_element_by_xpath(variables.locatorRepo['submit_button']).click()

        #validation
        saveMsg=self.driver.find_element_by_xpath("//*[text()='User Updated Successfully. ']").text
        assert (saveMsg==variables.expectedValues['expectedSaveMsg'])
        actual_value=self.driver.find_element_by_xpath(variables.locatorRepo[field+'_Actual']).text
        assert (actual_value==expected_value)

    def deleteUser(self,user_id):
        locator=variables.locatorRepo['Delete'].format(user_id)
        print(locator)
        self.wait_for_locator(locator)
        self.driver.find_element_by_xpath(locator)
        self.element_does_not_exist(variables.locatorRepo['Delete'].format(user_id))
