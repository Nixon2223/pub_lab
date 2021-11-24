import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer(1, 0, 15.55, 18)



        

    def test_customer_has_id(self):
        self.assertEqual(1, self.customer.id)

    def test_customer_has_wallet(self):
        self.assertEqual(15.55, self.customer.wallet)
    
    def test_decrease_wallet(self):
        self.customer.decrease_wallet(3)
        self.assertEqual(12.55, self.customer.wallet)

    def test_customer_has_drunkness(self):
        self.assertEqual(0,self.customer.drunkness)

    def test_customer_drunkness_can_increase(self):
        self.customer.increase_drunkness(1)
        self.assertEqual(1,self.customer.drunkness)