import unittest
from selenium import webdriver

class MyClass(unittest.TestCase):

    def test_login(self):
        print('test Login')
    def test_printing(self):
        print('test Printing')
    @classmethod
    def setUp(self):
        print('Before each method')
    @classmethod
    def tearDown(self):
        print('After each method...')

if __name__ == "__main__":
    unittest.main()

