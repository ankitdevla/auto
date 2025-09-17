
from pages.pageDynamicControl import DynamicControlPage
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.mark.usefixtures("login")
def test_dynamic_control(login):

    """Test case for adding and removing elements."""
    dynamic_control_page = DynamicControlPage(login)
    
    dynamic_control_page.clickDynamicControlLink()
    
    dynamic_control_page.clickCheckBox().click()

    dynamic_control_page.clickCheckBoxButtonForRemove().click()

    dynamic_control_page.clickCheckBoxButtonForAdd().click()   

    dynamic_control_page.clickNewCheckBox().click()
    dynamic_control_page.clickEnableButton().click()

    dynamic_control_page.clickInputBox().send_keys("Hello World")
    time.sleep(5)
    

    dynamic_control_page.backDriver()