import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # Suppress TensorFlow logs


@pytest.fixture(scope="session")
def setup():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    print("WebDriver initialized successfully.")
    yield driver    
    driver.quit()
    print("WebDriver closed.")



@pytest.fixture(scope="session")
def login(setup):
    # Perform login and return the driver
    driver = setup
    driver.implicitly_wait(10)  # Wait for up to 10 seconds
    driver.get("https://the-internet.herokuapp.com/")
    return driver
    



def pytest_collection_modifyitems(session, config, items):
    # Define custom priority order for test files
    priority = {
        "test_title.py": 1,
        "test_AddRemoveElement.py": 2,
       
    }
    # Sort test items based on file priority
    items.sort(key=lambda item: priority.get(item.fspath.basename, 99))  # Default priority = 99 (low)

    