
from pages.pageDropDown import DropDownPage
from selenium.webdriver.common.by import By
import pytest

import time

@pytest.mark.usefixtures("login")
def test_drag_adn_drop(login):

    """Test case for Drop down."""
    drop_and_down_page = DropDownPage(login)
    time.sleep(15)
    drop_and_down_page.clickDropDownLink()

    time.sleep(10)
    drop_and_down_page.select_dropdown_option()
    # Adding a sleep to observe the result, can be removed in production code   

    