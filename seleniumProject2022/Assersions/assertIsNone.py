import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Test(unittest.TestCase):
    def test_testName(self):
        service= Service('C://Drivers/chromedriver.exe')
        driver= webdriver.Chrome(service=service)
        driver.get('https://google.com')
        # driver=None
        driver.maximize_window()
        title=driver.title

        self.assertIsNone(driver)  #False - TEST SHOULD FAILED if rows 11-12 are enabled , Row 10 in comment
        # self.assertIsNone(driver)    #True when rows 11-12 in comment

if __name__ == "__main__":
    unittest.main()


