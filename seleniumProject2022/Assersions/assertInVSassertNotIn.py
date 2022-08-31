import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        list =["python", "hebrew", "linux", "windows"]
        # self.assertIn("hebrew1", list, "The item was NOT found in the list ") #FALSE
        # self.assertNotIn("hebrew2", list) #True
        self.assertNotIn("hebrew", list) #False - because it is in the list

if __name__ == "__main__":
    unittest.main()
