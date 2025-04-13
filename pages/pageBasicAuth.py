from selenium.webdriver.common.by import By



class BasicAuthPage:
    """Page object for the Add/Remove Elements page."""

    def __init__(self, driver):
        self.driver = driver
        
        self.BasicAuthLink = "//a[@href='/basic_auth']"

    
    def clickAddRemoveElementLink(self):
        self.driver.find_element(By.XPATH, self.BasicAuthLink).click()

    def backDriver(self):
        self.driver.back()


