class Searching:
    textbox_search_id = "SearchEmail"
    textbox_company_id = "SearchCompany"
    textbox_FirstName_id = "SearchFirstName"
    textbox_LastName_id = "SearchLastName"
    textbox_IpAddress_id = "SearchIpAddress"
    button_Search_id = "search-customers"
    table_xpath = "//*[@role ='grid']"
    tblSearchResults_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"


    def __init__(self, driver):
        self.driver = driver

    def setSearch(self, Email):
        self.driver.find_element_by_id(self.textbox_search_id).clear()
        self.driver.find_element_by_id(self.textbox_search_id).send_keys(Email)

    def setCompany(self, CompanyName):
        self.driver.find_element_by_id(self.textbox_company_id).clear()
        self.driver.find_element_by_id(self.textbox_company_id).send_keys(CompanyName)

    def setNameF(self, FirstName):
        self.driver.find_element_by_id(self.textbox_FirstName_id).clear()
        self.driver.find_element_by_id(self.textbox_FirstName_id).send_keys(FirstName)

    def setNameL(self, LastName):
        self.driver.find_element_by_id(self.textbox_LastName_id).clear()
        self.driver.find_element_by_id(self.textbox_LastName_id).send_keys(LastName)

    def setIpAddress(self, IpAdd):
        self.driver.find_element_by_id(self.textbox_IpAddress_id).clear()
        self.driver.find_element_by_id(self.textbox_IpAddress_id).send_keys(IpAdd)

    def clickOnSearch(self):
        self.driver.find_element_by_id(self.button_Search_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_element_by_xpath(self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_element_by_xpath(self.tableColumns_xpath))

    def searchCustomerByEmail(self, Email):
        flag = False
        for x in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            emailId = table.find_element_by_xpath("//table[@id='customer-grid']/tbody/tr["+str(x)+"]td[2]").text
            if emailId == Email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for x in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            name = table.find_element_by_xpath("//table[@id='customer-grid']/tbody/tr["+str(x)+"]td[3]").text
            if name == Name:
                flag = True
                break
        return flag
