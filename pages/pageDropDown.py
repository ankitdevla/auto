from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DropDown:
    """Page object for the Add/Remove Elements page."""

    def __init__(self, driver):
        self.driver = driver
        
        self.DropDownLink = "//a[@href = '/dropdown']"


        
    def clickDropDownLink(self):
        self.driver.find_element(By.XPATH, self.DropDownLink).click()

    def backDriver(self):
        self.driver.back()

    def dropDown(self):
        """Method to perform drag and drop action."""
        select_element = self.driver.find_element(By.ID, 'dropdown')
        select = Select(select_element)
        select.select_by_visible_text('Option 2')
