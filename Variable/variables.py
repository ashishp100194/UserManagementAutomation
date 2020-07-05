objectRepo={
    "url":"https://ankitairen.github.io/",
    "admin_user":"admin",
    "admin_password":"Admin123#",
    "user_1":"test_automation",
    "password_1":"Admin123#"
}

locatorRepo={
    "user_id":"//*[@id='userid']",
    "password":"//*[@id='password']",
    "remember_me":"//*[@class='remember-me']/input",
    "submit_button":"//*[@type='submit']",
    "AddUser":"//*[@ui-sref='adduser']",
    "ViewUsers":"//*[@ui-sref='viewuser']",
    "Search":"//*[contains(text(),'Search')]//following-sibling::input",
    "Delete":"//td[contains(text(),{})]/following-sibling::td/span",
    "MyProfile":"//*[@ui-sref='myprofile']",
    "SignOut":"//*[@ui-sref='login']",
    "User_Id":"//*[@name='id']",
    "Password":"//*[@name='password']",
    "First_Name":"//*[@name='firstname']",
    "Last_Name":"//*[@name='lastname']",
    "Password_Actual":"//*[contains(text(),'Password')]//following-sibling::span",
    "First_Name_Actual":"//*[contains(text(),'First Name')]//following-sibling::span",
    "Last_Name_Actual":"//*[contains(text(),'Last Name')]//following-sibling::span",
    "Invalid_Creds":"//*[@class='invalid-creds']"
}

expectedValues={
    "expectedSaveMsg":"User Updated Successfully. ",
    "userAlreadyExists":"This userid already exists. Please enter another userid. ",
    "invalidCredsMsg":"Invalid UserId. Please try again "
}