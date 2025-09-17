
from pages.pageDragAndDrop import DragAndDropPage
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("login")
def test_drag_adn_drop(login):

    """Test case for adding and removing elements."""
    drag_and_drop_page = DragAndDropPage(login)
    drag_and_drop_page.clickDragAndDropLink()
    drag_and_drop_page.dragAndDrop()
    drag_and_drop_page.backDriver()
    import time
    time.sleep(10)
