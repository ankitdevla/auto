
from pages.pageDropDown import DropDown
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("login")
def test_drag_adn_drop(login):

    """Test case for adding and removing elements."""
    select_page = DropDown(login)
    select_page.clickDropDownLink()
    select_page.dropDown()
    select_page.backDriver()
    import time
    time.sleep(10)
