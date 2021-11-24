import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drink1 = Drink("pint of beer", 4.50, True, 3)
        self.drink2 = Drink("still water", 0, False, 0)
        self.customer1 = Customer(1, 0, 22.50, 19)
        self.customer2 = Customer(2, 0, 15, 18)
        self.customer3 = Customer(3, 0, 11.5, 17)
        self.customer4 = Customer(3, 11, 11.5, 20)
        self.pub.drinks_list = [self.drink1, self.drink2]
    

    
    
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)
    
    def test_count_drinks_list(self):
        self.assertEqual(2, self.pub.count_drinks_list())

    def test_add_drink_to_list(self):
        new_drink = Drink("pint of cider", 4, True, 3)
        self.pub.add_drink_to_list(new_drink)
        self.assertEqual(3, self.pub.count_drinks_list())

    def test_increase_till(self):
        self.pub.increase_till(10)
        self.assertEqual(110, self.pub.till)

    def test_sell_drink(self):
        self.pub.sell_drink(self.drink1, self.customer1)
        self.pub.sell_drink(self.drink1,self.customer4)
        self.assertEqual(104.5, self.pub.till)
        self.assertEqual(18, self.customer1.wallet)
        self.assertEqual(11,self.customer4.drunkness)

    def test_sell_to_underage(self):
        self.pub.sell_drink(self.drink1, self.customer3)
        self.assertEqual(100, self.pub.till)
        self.assertEqual(11.5, self.customer3.wallet)
        self.assertEqual("Please choose a soft drink: ['still water']", self.pub.sell_drink(self.drink1, self.customer3) )
    
    def test_check_customer_over_18(self):
        self.assertEqual(True, self.pub.check_customer_age(self.customer1))
        self.assertEqual(True, self.pub.check_customer_age(self.customer2))
        self.assertEqual(False, self.pub.check_customer_age(self.customer3))
    
    def test_drunkness_increased(self):
        
        self.pub.sell_drink(self.drink1, self.customer1)
        self.pub.sell_drink(self.drink1, self.customer3)
        self.assertEqual(3, self.customer1.drunkness)
        self.assertEqual(0, self.customer3.drunkness)
