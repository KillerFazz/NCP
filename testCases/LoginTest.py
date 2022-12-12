# import time

import pytest
from pageObjects.LoginPage import LoginPge
# from selenium import webdriver
from utilities.customlogger import LogGen
from utilities.ReadProperties import Readconfig
import time

class Test__001__Login:
    BaseURL = Readconfig.getApplicationURl()
    username = Readconfig.getUserName()
    password = Readconfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_HomePageTitle(self, setup):
        self.logger.info("************************** Started Testing ****************")
        self.logger.info("************************** Verifying Home Page Title ****************")
        self.driver = setup
        # self.driver = webdriver.Chrome()
        self.driver.get(self.BaseURL)
        self.driver.maximize_window()
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.logger.info("************************** Home page title is Passed ***************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "HomePageTitle.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.driver = setup
        # self.driver = webdriver.Chrome()
        self.lp = LoginPge(self.driver)
        self.driver.maximize_window()
        time.sleep(5)
        self.lp.setUserName(self.username)
        time.sleep(5)
        self.lp.setPassword(self.password)
        time.sleep(5)
        self.lp.clickLogin()
        self.driver.close()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce admin":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False
