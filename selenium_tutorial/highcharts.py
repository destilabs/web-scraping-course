from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.setups import get_local_safe_setup

import pandas as pd

def parse_high_charts(driver):
    dates = driver.execute_script("return Highcharts.charts[0].series[0].data.map(x => x.series).map(x => x.xData)[0].map(x => new Date(x).toISOString())")
    values = driver.execute_script("return Highcharts.charts[0].series[0].data.map(x => x.series).map(x => x.yData)[0]")

    return pd.DataFrame({'date': dates, 'value': values})

if __name__ == '__main__':
    driver = get_local_safe_setup()

    driver.get('https://www.worldweatheronline.com/brussels-weather/be.aspx')

    # 1. Hide the cookie banner
    cookie_banner = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'css-47sehv'))
    )

    # 2. Scroll down to plot to make it render
    driver.execute_script('window.scrollBy(0, 1000);')

    # 3. Execute script and capture results
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'highcharts-container'))
    )

    df = parse_high_charts(driver)

    print(df.head())

    df.to_csv('highcharts.csv')

    driver.quit()