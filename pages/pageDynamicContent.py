from selenium.webdriver.common.by import By


class DynamicContentPage:
    """Page object for the Add/Remove Elements page."""

    def __init__(self, driver):
        self.driver = driver
        
        self.DynamicContentLink = "//a[@href='/dynamic_content']"
        self.Click_HereLink = "//a[text()='click here']"
        self.text1 = "(//div[@class = 'large-10 columns'])[1]"
        self.text2 = "(//div[@class = 'large-10 columns'])[2]"
        self.text3 = "(//div[@class = 'large-10 columns'])[3]"
        

    def clickDynamicContentLink(self):
        self.driver.find_element(By.XPATH, self.DynamicContentLink).click()

    def backDriver(self):
        self.driver.back()

    def clickHere(self):
        """Method to perform drag and drop action."""
        self.driver.find_element(By.XPATH, self.Click_HereLink).click()

    def getText1(self):
        return self.driver.find_element(By.XPATH, self.text1).text

    def getText2(self):
        return self.driver.find_element(By.XPATH, self.text2).text

    def getText3(self):
        return self.driver.find_element(By.XPATH, self.text3).text