from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pprint
import time

class config:

    def start_browser(self,browser):
        """
        This function initiates browser based upon the browser parameter passed (chrome or firefox).

        As returns the driver object which can be used acrossed.

        :param browser: chrome, firefox
        :param device: desktop
        :return: self.driver object
        """

        if browser=="chrome":
            chromedriver="../ExternalDependency/chromedriver.exe"
            self.driver=webdriver.Chrome(chromedriver)

        elif browser=="firefox":
            geckodriver="../ExternalDependency/geckodriver.exe"
            self.driver=webdriver.Firefox(geckodriver)

        self.wait = WebDriverWait(self.driver, 5)
        self.action = ActionChains(self.driver)
        self.driver.maximize_window()

        return self.driver

    def wait_for_locator(self,xpath):
        """
        Waits until the expected condition is achieved.
        The wait time is defined under self.wait = 30
        If the element is not present in first attempt, this function will retry to locate it once after self.wait timeout

        :param xpath: identifier/locator
        """

        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
        except:
            print("Did not get after 1 attempt")
            print(xpath)
            self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))

    def element_does_not_exist(self,xpath):
        element = self.driver.find_element_by_xpath(xpath).is_displayed()
        if element:
            raise Exception("Element found")
        else:
            pass