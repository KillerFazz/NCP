import pytest
from pageObjects.AddCustomersPage import AddCustomer
from pageObjects.LoginPage import LoginPge
from pageObjects.SearchingPage import Searching
from selenium import webdriver
from utilities.customlogger import LogGen
from utilities.ReadProperties import Readconfig
import time
import random
import string

class Test_SearchCustomerByDEmail__004:
    BaseURL = Readconfig.getApplicationURl()
    username = Readconfig.getUserName()
    password = Readconfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_SearchCustomerByEmail(self, setup):
        self.logger.info("*********************--Test__004__Searching--************************")
        self.driver = setup
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        self.Lp = LoginPge(self.driver)
        self.Lp.setUserName(self.username)
        self.Lp.setPassword(self.password)
        time.sleep(5)
        self.Lp.clickLogin()
        self.logger.info("************************ Login Successful ***************")

        self.logger.info("*************************** Starting Search Customer by Email **************")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomerMenu()
        self.addCust.clickOnCustomerSubMenu()

        self.logger.info("*************************** Searching Customer by Email **************")

        self.SearchCust = Searching(self.driver)
        self.SearchCust.setSearch("	mithileshkumar2831999@gmail.com")
        self.SearchCust.clickOnSearch()
        time.sleep(5)
        status = self.SearchCust.searchCustomerByEmail("mithileshkumar2831999@gmail.com")
        assert True==status

        self.logger.info("*************************** TC_SearchCustomerByEmail_004 Finished--****************************")
        self.driver.close()
