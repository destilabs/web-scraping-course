from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import os

def get_safe_setup():
    options = ChromeOptions() 
    options.add_argument("--disable-dev-shm-usage") 
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")

    driver = webdriver.Remote("http://127.0.0.1:4444", desired_capabilities = options.to_capabilities())

    return driver

def get_local_safe_setup():
    user_data_dir = os.path.join(os.path.dirname(__file__), "..", "..", "..", "user_data")

    options = ChromeOptions() 
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    options.add_argument("--user-data-dir=./user_data")

    driver = Chrome(desired_capabilities = options.to_capabilities())

    return driver