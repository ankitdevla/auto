
from pages.pageDynamicContent import DynamicContentPage
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.mark.usefixtures("login")
def test_dynamic_content(login):

    """Test case for adding and removing elements."""
    dynamic_content_page = DynamicContentPage(login)
    
    dynamic_content_page.clickDynamicContentLink()
    text3_before = dynamic_content_page.getText3()
    dynamic_content_page.clickHere()
    
    text3_after = dynamic_content_page.getText3()


    # assert text3_before != text3_after, "Text did not change after clicking 'click here' link"
    dynamic_content_page.backDriver()