import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



import os
# os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # Suppress TensorFlow logs


@pytest.fixture(scope="session")
def setup():

    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    # chrome_options = Options()
    # chrome_options.add_argument("--incognito")
    # service = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    print("WebDriver initialized successfully.")
    yield driver    
    driver.quit()
    print("WebDriver closed.")



@pytest.fixture(scope="session")
def login(setup):
    # Perform login and return the driver
    driver = setup
    driver.get("https://the-internet.herokuapp.com/")
    return driver
    

# conftest.py
def pytest_collection_modifyitems(config, items):
    # Define priority order
    priority = {
        "test_title": 1,
        "test_Select": 2,
        # "test_logout": 3,
    }

    # Sort items by priority
    items.sort(key=lambda item: priority.get(item.name, 999))
