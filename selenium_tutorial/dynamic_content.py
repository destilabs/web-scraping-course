from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.setups import get_local_safe_setup

if __name__ == "__main__":
    driver = get_local_safe_setup()

    driver.get("https://scrollmagic.io/examples/advanced/infinite_scrolling.html")

    for i in range(0, 4):
        distance = (i + 1) * 500

        driver.execute_script("window.scrollTo(0, {});".format(distance))

        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.ID, "loader"))
        )

    elements = driver.find_elements_by_class_name('box1')

    print("\n".join([e.get_attribute('style') for e in elements]))

    driver.quit()