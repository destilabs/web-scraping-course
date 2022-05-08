from common.setups import get_safe_setup, get_local_safe_setup
from common.helpers import get_element_by_selector

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

if __name__ == "__main__":
    driver = get_safe_setup()

    driver.get("https://devpost.com/hackathons")

    WebDriverWait(driver, 5).until(
       lambda driver: driver.find_element(By.CLASS_NAME, "hackathons-container")
    )

    hackathons = driver.find_elements(By.CLASS_NAME, "content")
    for i, hackathon in enumerate(hackathons):
       print(f'{i + 1}.', 
            get_element_by_selector(hackathon, 'h3'),
            get_element_by_selector(hackathon, '.mb-4'),
            get_element_by_selector(hackathon, '.mb-6'),
            get_element_by_selector(hackathon, '.prizes-and-participants'))

    driver.quit()