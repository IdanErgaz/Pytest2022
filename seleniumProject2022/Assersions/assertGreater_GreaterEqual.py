import unittest

class Test(unittest.TestCase):
    def testName(self):
        #assertGreater
        # self.assertGreater(3, 2) #TRUE
        # self.assertGreater(2, 2) #FALSE
        self.assertGreaterEqual(2,2)  #TRUE
if __name__ == "__main__":
    unittest.main()


