import unittest
from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignupTest
from Package2.TC_PaymentTest import PaymentTest
from Package2.TC_PaymentReturns import ReturnsTest

#get all the tests from LoginTest,SignupTest, PaymentTest, ReturnTest
tc1= unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2= unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3= unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4= unittest.TestLoader().loadTestsFromTestCase(ReturnsTest)

#creating the test suit
sanityTestSuit= unittest.TestSuite([tc1, tc2]) #sanity test suit

#functional test suit
functionalTestSuit = unittest.TestSuite([tc3,tc4])

#master test suit
masterTestSuit = unittest.TestSuite([tc1, tc2, tc3, tc4])


#Main
# unittest.TextTestRunner().run(sanityTestSuit) #for running the Sanity suit
# unittest.TextTestRunner().run(functionalTestSuit)  #run only the Functional test suit
unittest.TextTestRunner().run(masterTestSuit)  #run only the MASTER test suit

# if __name__ == "__main__":
#     unittest.main()