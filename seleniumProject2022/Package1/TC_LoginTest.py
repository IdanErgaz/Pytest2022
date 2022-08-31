import unittest
class LoginTest(unittest.TestCase):
    def test_loginByEmail(self):
        print('Login by email test ')
        self.assertTrue(True)

    def test_loginByFacebook(self):
        print('login by facebook')
        self.assertTrue(True)

    def test_loginByTwitter(self):
        print('login by Twitter')
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
