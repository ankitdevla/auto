from selenium.webdriver.common.by import By



class AddRemoveElementPage:
    """Page object for the Add/Remove Elements page."""

    def __init__(self, driver):
        self.driver = driver
        
        self.AddRemoveElementLink = "//a[@href='/add_remove_elements/']"
        self.AddElementButton = "//button[text()='Add Element']" 
        self.DeleteElementButton = "//button[text()='Delete']" 


    def clickAddRemoveElementLink(self):
        self.driver.find_element(By.XPATH, self.AddRemoveElementLink).click()

    def clickAddElementButton(self):
        self.driver.find_element(By.XPATH, self.AddElementButton).click()

        
    def clickDeleteElementButton(self):
        self.driver.find_element(By.XPATH, self.DeleteElementButton).click()

    def backDriver(self):
        self.driver.back()
