import unittest
class PaymentTest(unittest.TestCase):
    def test_paymentInDollars(self):
        print('payment  in dollars')
        self.assertTrue(True)
    def test_paymentInRupees(self):
        print('paymennt in rupees')
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()