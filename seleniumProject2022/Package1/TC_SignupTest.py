import unittest
class SignupTest(unittest.TestCase):
    def test_signupByEmail(self):
        print('signup by email')
        self.assertTrue(True)
    def test_signupByFacebook(self):
        print('signup by facebook')
        self.assertTrue(True)


    def test_signupByTwitter(self):
        print('signup by Twitter')
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()