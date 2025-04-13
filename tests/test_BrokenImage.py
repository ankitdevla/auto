
from pages.pageBrokenImage import BrokenImagePage 
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.mark.usefixtures("login")
def test_broken_image(login):

    """Test case for adding and removing elements."""

    
    broken_image_page = BrokenImagePage(login)


    broken_image_page.clickBrokenImagelink()

    broken_image_page.backDriver()