from pageObjects.SearchingPage import Searching
from pageObjects.LoginPage import LoginPge
from selenium import webdriver
from utilities.customlogger import LogGen
from utilities.ReadProperties import Readconfig
import time
# import random
# import string

class Test_004_Searching:
    BaseURL = Readconfig.getApplicationURl()
    username = Readconfig.getUserName()
    password = Readconfig.getPassword()

    logger = LogGen.loggen()

    def test_AddCust(self, setup):
        self.logger.info("*********************Test__003__AddCustomer************************")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.Lp = LoginPge(self.driver)
        self.Lp.setUserName(self.username)
        self.Lp.setPassword(self.password)
        time.sleep(5)
        self.Lp.clickLogin()
        self.logger.info("************************ Login Successfully Completed ***************")

        self.logger.info("*************************** Starting Add Customer Test **************")

        self.Src = Searching(self.driver)
        self.Src.setSearch("victoria_victoria@nopCommerce.com")

        self.driver.close()