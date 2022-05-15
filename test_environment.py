import unittest
import importlib

class TestEnvironment(unittest.TestCase):
    def test_package_installation(self):
        bs4 = importlib.import_module('bs4')
        requests = importlib.import_module('requests')
        selenium = importlib.import_module('selenium')
        unittest = importlib.import_module('unittest')
        dotenv = importlib.import_module('dotenv')
        twocaptcha = importlib.import_module('twocaptcha')
        pillow = importlib.import_module('pillow')
        jupyter = importlib.import_module('jupyter')

        self.assertTrue(bs4, 'bs4 is not installed')
        self.assertTrue(requests, 'requests is not installed')
        self.assertTrue(selenium, 'selenium is not installed')
        self.assertTrue(unittest, 'unittest is not installed')
        self.assertTrue(dotenv, 'dotenv is not installed')
        self.assertTrue(twocaptcha, 'twocaptcha is not installed')
        self.assertTrue(pillow, 'pillow is not installed')
        self.assertTrue(jupyter, 'jupyter is not installed')

    @unittest.skip('This test is not implemented yet')
    def test_selenium_local_is_up_and_running(self):
        from common.setups import get_local_safe_setup

        driver = get_local_safe_setup()
        driver.get('https://www.google.com/')

        self.assertEqual(driver.current_url, 'https://www.google.com/', 'Selenium Grid is not ready. Check installation tutorial: https://github.com/destilabs/web-scraping-course#selenium-installation')

    def test_docker_selenium_is_up_and_running(self):
        import requests
        response = requests.get('http://localhost:4444/status')

        self.assertEqual(response.status_code, 200, 'Selenium Grid is not ready. Check installation in Docker tutorial: https://github.com/destilabs/web-scraping-course#docker-installation')
        self.assertEqual(response.json()['value']['ready'], True, 'Selenium Grid is not ready. Check installation in Docker tutorial: https://github.com/destilabs/web-scraping-course#docker-installation')

        