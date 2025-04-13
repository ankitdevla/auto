from selenium.webdriver.common.by import By



class CheckBoxPage:
    """Page object for the Add/Remove Elements page."""

    def __init__(self, driver):
        self.driver = driver
        
        self.CheckBoxLink = "//a[text()='Checkboxes']"
        self.CheckBox = "//form[@id ='checkboxes']/input[1]"
        self.UnCheckBox = "//form[@id ='checkboxes']/input[2]"
        
    def clickCheckBoxLink(self):
        self.driver.find_element(By.XPATH, self.CheckBoxLink).click()

    def clickCheckBox(self):
        self.driver.find_element(By.XPATH, self.CheckBox).click()

    def clickUnCheckBox(self):
        self.driver.find_element(By.XPATH, self.UnCheckBox).click()


    def backDriver(self):
        self.driver.back()
