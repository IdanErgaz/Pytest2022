import unittest

#The tests with the conditions and the reasons will be mentioned as SKIPPED after running.
#The test that just skipped with no reason and condition wont be run at all and the user  doesn't know that it was skipped

class appTesting(unittest.TestCase):
    def test_search(self):
        print('This is the search test.')

    @unittest.SkipTest  #skipping that test
    def test_advancedSearch(self):
        print('ADVANCED search ')
    @unittest.skip('I am skipping "test_prepaidRecharged" test just because')
    def test_prepaidRecharged(self):
        print('prepaidRecharge test')

    def test_postPaidRecharge(self):
        print('this is postPaidRecharge test')
    @unittest.skipIf(1==1, "because the condition test_loginByEmail test will be skipped!")
    def test_loginByEmail(self):
        print('login by email test')

    def test_loginByTwitter(self):
        print('login by twitter')

if __name__ ==  "__main__":
    unittest.main()

