from common.setups import get_safe_setup, get_local_safe_setup
from common.helpers import get_element_by_selector

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

if __name__ == "__main__":
    driver = get_local_safe_setup()

    driver.get("https://quotes.toscrape.com/")

    WebDriverWait(driver, 5).until(
         lambda driver: driver.find_element(By.CLASS_NAME, "quote")
    )

    # Get login link
    login_link = driver.find_element(By.LINK_TEXT, "Login")
    login_link.click()

    # Get username and password
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    username.send_keys("username")
    password.send_keys("password")

    # Get login button
    login_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    login_button.click()
    
    try:
        assert(driver.find_element(By.LINK_TEXT, "Logout").is_displayed())
        print('Login successful!')
    except NoSuchElementException:
        print('Login failed!')

    # Quit driver
    driver.quit()