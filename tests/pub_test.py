import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drink = Drink("pint of beer", 4.50, True, 3)
        self.customer = Customer(1, 0, 22.50)
        self.pub.drinks_list = [self.drink]

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)
    
    def test_count_drinks_list(self):
        self.assertEqual(1, self.pub.count_drinks_list())

    def test_add_drink_to_list(self):
        new_drink = Drink("still water", 0, False, 0)
        self.pub.add_drink_to_list(new_drink)
        self.assertEqual(2, self.pub.count_drinks_list())

    def test_increase_till(self):
        self.pub.increase_till(10)
        self.assertEqual(110, self.pub.till)

    # def test_sell_drink(self, drink, customer):
    #     sell_drink(drink, customer)
    #     self.assertEqual(104.5, self.pub.till)
    #     self.assertEqual(18, self.customer1.wallet)
