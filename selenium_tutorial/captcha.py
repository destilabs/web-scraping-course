from common.setups import get_local_safe_setup
from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha

import os
import time
from dotenv import load_dotenv

def solve_captcha(url):
    solver_config = {
        'apiKey': os.getenv('TWO_CAPTCHA_API_KEY'),
        'defaultTimeout': 120,
        'recaptchaTimeout': 600,
        'pollingInterval': 10,
    }

    solver = TwoCaptcha(**solver_config)

    try:
        result = solver.recaptcha(
            sitekey=os.getenv('CAPTCHA_SITE_KEY'),
            url=url
        )

    except Exception as e:
        print(e)
        return False

    return result

def make_input_visible(response):
    google_captcha_response_input = driver.find_element(
                By.ID, 'g-recaptcha-response')

    # make input visible
    driver.execute_script(
        "arguments[0].setAttribute('style','display: block; type: text; visibility:visible;');",
        google_captcha_response_input)

    # input the code received from 2captcha API
    google_captcha_response_input.send_keys(response.get('code'))

    # hide the captcha input
    driver.execute_script(
        "arguments[0].setAttribute('style', 'display:none;');",
        google_captcha_response_input)


def complete_form(driver):
    # Enter the Name
    name_input = driver.find_element(By.ID, 'name')
    name_input.send_keys('John Doe')

    # Enter the Email
    email_input = driver.find_element(By.ID, 'email')
    email_input.send_keys('test_emai@gmail.com')

    # Enter the Phone Number
    phone_input = driver.find_element(By.ID, 'phone')
    phone_input.send_keys('+1 (123) 456-7890')

    # Enter the Message
    message_input = driver.find_element(By.ID, 'comment-content')
    message_input.send_keys('Hello World!')

if __name__ == "__main__":   
    load_dotenv()

    driver = get_local_safe_setup()

    url = os.getenv('SITE_URL')

    driver.get(url)

    try:
        complete_form(driver)
    except:
        print('Could not complete form')
        driver.quit()
        exit(1)
        
    response = solve_captcha(url)

    if response:
        make_input_visible(response)

    # submit the form
    driver.find_element(By.ID, 'send-message').click()

    time.sleep(5)

    driver.quit()
