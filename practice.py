from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time




driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/")
    driver.maximize_window()
  
    
    assert driver.title == "The Internet"
    print("✅ Login successful!")

  

finally:
    time.sleep(3)
    driver.quit()
