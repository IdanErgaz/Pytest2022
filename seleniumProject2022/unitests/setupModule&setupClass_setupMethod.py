import unittest

def setUpModule():
    print('setup MODULE - running before all the classes method ')#will be run before executing any class  or any method in the test class
def tearDownModule():
    print('tearDownModule...') #will be run after completing everything which is presented in python mpdule
class Login(unittest.TestCase):
    def test_loginByEmai(self):
        print('Login by EMAIL')
    def test_loginByPassword(self):
        print('Login by Password')
    @classmethod
    def setUp(self): #will be run before each  method
        print('Run BEFORE each method...')
    @classmethod
    def tearDown(self):
        print('Run after each method')  #will be run AFTER  each  method
    @classmethod
    def setUpClass(cls):
        print('RUN before all the methods ONE TIME!!!!') #will be run BEFORE starting running the class method ONCE
    @classmethod
    def tearDownClass(cls):
        print('Run ONE time AFTER all methode finish to run ')#will be run AFTER  starting running the class method ONCE
if __name__ =="__main__":
    unittest.main()