from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DynamicControlPage:
    """Page object for the Add/Remove Elements page, with explicit waits."""

    def __init__(self, driver, timeout=6):
        self.driver = driver
        self.timeout = timeout

        self.DynamicControlLink = (By.XPATH, "//a[@href='/dynamic_controls']")
        self.ClickCheckBox = (By.XPATH, "//div[@id='checkbox']//input")
        self.ClickCheckBoxRemoveButton = (By.XPATH, "//button[text()='Remove']")
        self.ClickCheckBoxAddButton = (By.XPATH, "//button[text()='Add']")
        self.ClickNewCheckBoxButton = (By.XPATH, "//input[@id='checkbox']")
        self.ClickEnableButton = (By.XPATH, "//button[text()='Enable']")
        self.ClickInputBox = (By.XPATH, "//form[@id='input-example']//input")

    def clickDynamicControlLink(self):
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.DynamicControlLink)
        ).click()

    def backDriver(self):
        self.driver.back()

    def clickCheckBox(self):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.ClickCheckBox)
        )

    def clickCheckBoxButtonForRemove(self):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.ClickCheckBoxRemoveButton)
        )

    def clickCheckBoxButtonForAdd(self):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.ClickCheckBoxAddButton)
        )

    def clickNewCheckBox(self):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.ClickNewCheckBoxButton)
        )

    def clickEnableButton(self):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.ClickEnableButton)
        )

    def clickInputBox(self):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.ClickInputBox)
        )