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

        #assertEqual(a,b) b should be like a
        # self.assertEqual("Googl6e", title, "Title is not the same!")

        # asserNotEqual(a,b)  b shoulNOT be like a
        # self.assertNotEqual("Google2", title, "The title is not like we expected")  #asserNotEqual

        
if __name__ == "__main__":
    unittest.main()