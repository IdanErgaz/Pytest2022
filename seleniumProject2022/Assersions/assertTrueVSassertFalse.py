import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Test(unittest.TestCase):
    def test_testName(self):
        service= Service('C://Drivers/chromedriver.exe')
        driver= webdriver.Chrome(service=service)
        driver.get('https://google.com')
        driver.maximize_window()
        title=driver.title

        # self.assertTrue(title == 'Google')  #True
        self.assertFalse(title =='dsdsds')  #False

if __name__ == " __main__":
    unittest.main()