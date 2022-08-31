import unittest

class Login(unittest.TestCase):
    def test_loginByEmai(self):
        print('Login by EMAIL')
    def test_loginByPassword(self):
        print('Login by Password')
    @classmethod
    def setUp(self):
        print('Run BEFORE each method...')
    @classmethod
    def tearDown(self):
        print('Run after each method')
    @classmethod
    def setUpClass(cls):
        print('RUN before all the methods ONE TIME!!!!')
    @classmethod
    def tearDownClass(cls):
        print('Run ONE time AFTER all methode finish to run ')
if __name__ =="__main__":
    unittest.main()