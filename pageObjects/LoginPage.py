# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By

class LoginPge:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//input[@class='button-1 login-button']"
    link_Logout_linkText = "Logout"

    def __init__(self, driver):
        self.driver = driver

    # def setUserName(self, username):
    #     self.driver.find_element(By.CSS_SELECTOR, self.textbox_username_selector).clear()
    #     self.driver.find_element(By.CSS_SELECTOR, self.textbox_username_selector).send_keys(username)
    #
    # def setPassword(self, password):
    #     self.driver.find_element(By.ID, self.textbox_password_id).clear()
    #     self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)
    #
    # def clickLogin(self):
    #     self.driver.find_element(By.XPATH, self.button_login_xpath).click()
    #
    # def clickLogout(self):
    #     self.driver.find_element(By.LINK_TEXT, self.link_Logout_linkText).click()

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_id(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_Logout_linkText).click()
