from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class DropDownPage:
    """Page object for the Dropdown Elements page."""

    def __init__(self, driver):
        self.driver = driver
        
        self.DropDownLink = "//a[text()='Dropdown']"
        self.DropDownButton = "//select[@id='dropdown']"
        
        

    def clickDropDownLink(self):
        self.driver.find_element(By.XPATH, self.DropDownLink).click()



    def select_dropdown_option(self):

        select = Select(self.DropDownButton)
        select.select_by_value(1)
        
        

