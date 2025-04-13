from conftest import *

@pytest.mark.usefixtures("login")
def test_title(login):
    login.get("https://the-internet.herokuapp.com/")
    assert login.title == "The Internet"


