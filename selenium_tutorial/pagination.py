from common.setups import get_local_safe_setup

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

import pandas as pd
import numpy as np

if __name__ == '__main__':
    driver = get_local_safe_setup()

    driver.get("https://quotes.toscrape.com/")

    def parse_titles():
        for p in range(1, 6):
            print(f"Page {p}")
            driver.get(f"https://quotes.toscrape.com/page/{p}/")

            titles = driver.find_elements_by_class_name("quote")

            yield [t.find_element_by_class_name('text').text for t in titles]

    pd.DataFrame(np.asarray(list(parse_titles()))).to_csv("titles.csv")

    driver.quit()