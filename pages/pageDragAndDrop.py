from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class DragAndDropPage:
    """Page object for the Add/Remove Elements page."""

    def __init__(self, driver):
        self.driver = driver
        
        self.DragAndDropLink = "//a[text() = 'Drag and Drop']"
        self.source = "//div[@id='column-a']"
        self.target = "//div[@id='column-b']"
    
        # Perform drag and drop
        actions = ActionChains(self.driver)
        actions.drag_and_drop(self.source, self.target).perform()


    def clickDragAndDropLink(self):
        self.driver.find_element(By.XPATH, self.DragAndDropLink).click()

    def backDriver(self):
        self.driver.back()

    def dragAndDrop(self):
        """Method to perform drag and drop action."""
        source = self.driver.find_element(By.XPATH, self.source)
        target = self.driver.find_element(By.XPATH, self.target)
        
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()
