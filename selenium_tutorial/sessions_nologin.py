from common.setups import get_safe_setup, get_local_safe_setup
from common.helpers import get_element_by_selector

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

import os
import json

if __name__ == "__main__":
    driver = get_local_safe_setup()

    driver.get("https://quotes.toscrape.com/")
    
    # Cookie management
    if os.path.exists("cookies.json"):
        with open("cookies.json", "r") as f:
            cookies = json.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)
    else:
        cookies = driver.get_cookies()
        with open("cookies.json", "w") as f:
            json.dump(cookies, f)

    driver.get("https://quotes.toscrape.com/")
    WebDriverWait(driver, 5).until(
         lambda driver: driver.find_element(By.CLASS_NAME, "quote")
    )

    try:
        assert(driver.find_element(By.LINK_TEXT, "Logout").is_displayed())
        print('Login successful!')
    except NoSuchElementException:
        print('Login failed!')
    
    # Quit driver
    driver.quit()