from selenium.webdriver.common.by import By



class BrokenImagePage:
    """Page object for the Broken Image page."""

    def __init__(self, driver):
        self.driver = driver
        
        self.AddRemoveElementLink = "//a[text() = 'Broken Images']"
        self.BrokenImageText = "//h3[text() = 'Broken Images']"

    def clickBrokenImagelink(self):
        self.driver.find_element(By.XPATH, self.AddRemoveElementLink).click()


    def backDriver(self):
        self.driver.back()



