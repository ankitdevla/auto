
from pages.pageBasicAuth import BasicAuthPage 
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.usefixtures("login")
def test_basic_auth(login):

    """Test case for adding and removing elements."""

    
    basic_auth_page = BasicAuthPage(login)
    basic_auth_page.clickAddRemoveElementLink()
    basic_auth_page.backDriver()

