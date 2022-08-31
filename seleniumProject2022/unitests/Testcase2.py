import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class OpenWebsite(unittest.TestCase):
    def test_open_google(self):
        service=Service('C:/Drivers/chromedriver.exe')
        self.driver=webdriver.Chrome(service=service)
        self.driver.get('https://google.co.il')
        self.driver.maximize_window()
        print('The title is:{}'.format(self.driver.title))
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()