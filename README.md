# UserManagementAutomation

Designed an UI automation framework to perform the CRUD operations on an usermanagement portal.
The scripting language used is Python and base automation framework as Pytest.

--What needs to be installed to execute the script?

Below are the dependencies which needs to be installed: 
Script Dependency: 
Programming Language: Python Version 3.8 
pip list: 
 - selenium=3.141.0
 - pytest=5.3.2

Note: The entire automation script is written in python 3.8 but has compatibility with python 2.7 version as well.

--How to execute?

The script can be executed with the below command from the command line: 
pytest test_user_crud_operation.py

Note: The prior installation needs to be done.

--What if the code doesn't work?

Ensure that all the dependencies as mentioned in the first point are installed correctly.

If any code issue arises, please revert back with the logs displayed at the command line.

You can also refer to the attached recording of the script execution.

The code may fail at test_verify_invalid_user(): try rerunning this case individually

Each test case in this file executes successfully if ran individually

--How the code components?

config.py contains generic functions: 
start_browser
 - wait_for_locator
 - element_does_not_exist

common.py contains customized functions:
 - login
 - logout
 - add user
 - delete user
 - update field

--Framework Used: I have created this project using Pytest framework with Python 3.8. 
Basically, this framework has 5 folders: 
 - ExternalDependency -- currently no external dependency is needed 
 - PythonLibrary -- contains all the global utils file
 - TestData -- contains dictionary for individual test data
 - TestSuite -- contains testcases to run
 - Variable -- Global variables

--What are the added testcases?

Currently, 10 testcases covering all the basic CRUD operation.

-- OS support?

As far as all the required dependencies are installed correctly, the script will run on Windows, Linux and Mac seamlessly.

Please revert back if any point seems unclear. Thank You :)
