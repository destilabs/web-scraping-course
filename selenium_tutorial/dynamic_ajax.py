from common.setups import get_local_safe_setup

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == '__main__':
    driver = get_local_safe_setup()

    driver.get("https://www.scrapethissite.com/pages/ajax-javascript/#2012")

    WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element(By.CLASS_NAME, 'film-title')
    )

    print([t.text for t in driver.find_elements_by_class_name('film-title')])

    driver.quit()