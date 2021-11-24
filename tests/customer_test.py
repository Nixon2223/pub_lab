import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer(1, 0, 15.55)

    def test_customer_has_id(self):
        self.assertEqual(1, self.customer.id)

    def test_customer_has_wallet(self):
        self.assertEqual(15.55, self.customer.wallet)