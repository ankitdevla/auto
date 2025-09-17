from conftest import *

@pytest.mark.usefixtures("login")
def test_title(login):
    assert login.title == "The Internet"


