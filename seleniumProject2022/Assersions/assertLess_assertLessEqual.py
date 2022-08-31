import unittest

class Test(unittest.TestCase):
    def testName(self):
        # self.assertLess(2,4)  #true
        # self.assertLess(2,2)  #false
        # self.assertLess(12,4)  #false
        self.assertLessEqual(4,4)  #true


if __name__ == "__main__":
    unittest.main()

