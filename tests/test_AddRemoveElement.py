
from pages.pageAddRemoveElement import AddRemoveElementPage
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.mark.usefixtures("login")
def test_add_remove_element(login):

    """Test case for adding and removing elements."""
    add_remove_element_page = AddRemoveElementPage(login)
    
    # Navigate to the Add/Remove Elements page
    # login.get("https://the-internet.herokuapp.com/")
    add_remove_element_page.clickAddRemoveElementLink()
    
    # Click the "Add Element" button
    add_remove_element_page.clickAddElementButton()
    time.sleep(2)
    
    # Verify that the "Delete" button is displayed
    assert login.find_element(By.XPATH, add_remove_element_page.DeleteElementButton).is_displayed(), "Delete button not displayed after adding element."
    
    # Click the "Delete" button
    add_remove_element_page.clickDeleteElementButton()
    
    add_remove_element_page.backDriver()
    # Verify that the "Delete" button is no longer displayed
    assert not login.find_elements(By.XPATH, add_remove_element_page.DeleteElementButton), "Delete button still displayed after removing element."
    
    