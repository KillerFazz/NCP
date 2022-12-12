
from pageObjects.AddCustomersPage import AddCustomer
from pageObjects.LoginPage import LoginPge
from selenium import webdriver
from utilities.customlogger import LogGen
from utilities.ReadProperties import Readconfig
import time
import random
import string


class Test_003_AddCustomer:
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

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomerMenu()
        self.addCust.clickOnCustomerSubMenu()

        self.addCust.clickOnAddNew()
        self.logger.info("************************* Providing Customer Details *****************")
        time.sleep(5)
        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("Test@9786")
        time.sleep(5)
        self.addCust.setCompanyName("Faz")
        self.addCust.setLastName("Shaikh")
        time.sleep(5)
        self.addCust.rdFemaleGender_id("Male")
        time.sleep(5)
        self.addCust.setDob("03/09/1996")
        time.sleep(5)
        self.addCust.setCompanyName("IT Software")
        time.sleep(5)
        self.addCust.setAdminContent("This is for testing..................")
        time.sleep(5)
        self.addCust.setCustomerRole("Guest")
        time.sleep(5)
        self.addCust.clickOnSave()

        self.logger.info("******************************* Saved Customer Info *******************************")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("**************** Add Customer Test Passed *********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_customer_scr.png")
            self.logger.info("**************************** Add Customer Test Failed *****************")
            assert True == False
        self.driver.close()
        self.logger.info("************************************ Ending Home Page Title Test **************")


def random_generator(size=8, char=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(char) for x in range(size))
