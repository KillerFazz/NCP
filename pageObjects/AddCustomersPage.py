import time
from selenium.webdriver.support.ui import Select

class AddCustomer:
    # Adding customer page
    linkCustomer_Menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    linkCustomer_SubMenu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    btnAddNew_xpath = "/html/body/div[3]/div[1]/form[1]/div/div/a"
    txtEmail_xpath = "//*[@id='Email']"
    txtPassword_xpath = "//*[@id='Password']"
    txtFirstName_xpath = "//*[@id='FirstName']"
    txtLastName_xpath = '//*[@id="LastName"]'
    rdMaleGender_id = 'Gender_Male'
    rdFemaleGender_id = 'Gender_Female'
    txtDob_xpath = '//*[@id="DateOfBirth"]'
    txtCompanyName_xpath = '//*[@id="Company"]'
    txtCustomerRoles_xpath = '//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div/div'
    lstItemAdministrators_xpath = '//*[@id="SelectedCustomerRoleIds_listbox"]/li[1]'
    lstItemRegistered_xpath = '//*[@id="d6063b5b-0561-4ba0-82a5-1477cfd35c66"]'
    lstItemGuest_xpath = '//*[@id="SelectedCustomerRoleIds_listbox"]/li[4]'
    lstItemVendors_xpath = '//*[@id="SelectedCustomerRoleIds_listbox"]/li[5]'
    lstMgrVendors_xpath = '//*[@id="SelectedCustomerRoleIds_listbox"]/li[9]'
    drpMgrOfVendor_xpath = '//*[@id="VendorId"]'
    txtContent_xpath = '//*[@id="AdminComment"]'
    btnSave_xpath = '/html/body/div[3]/div[1]/form/div[1]/div/button[1]'


    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.linkCustomer_Menu_xpath).click()

    def clickOnCustomerSubMenu(self):
        self.driver.find_element_by_xpath(self.linkCustomer_SubMenu_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btnAddNew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, firstname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lastname)

    def setDob(self, dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def setGender(self, gender):
        if gender == 'male':
            self.driver.find_element_by_xpath(self.rdMaleGender_id).click()
        elif gender == "Female":
            self.driver.find_element_by_xpath(self.rdFemaleGender_id).click()
        else:
            self.driver.find_element_by_xpath(self.rdFemaleGender_id).click()

    def setCustomerRole(self, role):
        self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).cilck()
        time.sleep(5)
        if role == "Registered":
            self.listItem = self.driver.find_element_by_xpath(self.lstItemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.lstItemAdministrators_xpath)
        elif role == 'Guest':
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstItemGuest_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element_by_xpath(self.lstItemVendors_xpath)
        else:
            self.driver.find_element_by_xpath(self.lstItemGuest_xpath).click()

    def setMangerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.lstMgrVendors_xpath))
        drp.select_by_visible_text(value)

    def setCompanyName(self, cname):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(cname)

    def setAdminContent(self, content):
        self.driver.find_element_by_xpath(self.txtContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).cilck()
