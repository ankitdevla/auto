
from pages.pageCheckBox import CheckBoxPage  
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("login")
def test_Check_box(login):

    """Test case for adding and removing elements."""

    
    broken_image_page = CheckBoxPage(login)
    broken_image_page.clickCheckBoxLink()

    broken_image_page.clickCheckBox()
    
    

@pytest.mark.usefixtures("login")
def test_Uncheck_box(login):

    """Test case for adding and removing elements."""

    
    broken_image_page = CheckBoxPage(login)


    broken_image_page.clickUnCheckBox()
    

    broken_image_page.backDriver()
    import time
    time.sleep(5)
    
