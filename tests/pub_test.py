import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.drink1 = Drink("pint of beer", 4.50, True, 3)
        self.drink2 = Drink("still water", 0, False, 0)
        self.food1 = Food("Pie", 5.50, 3)
        self.food2 = Food("sandwich", 4, 2)
        self.customer1 = Customer(1, 0, 22.50, 19)
        self.customer2 = Customer(2, 0, 15, 18)
        self.customer3 = Customer(3, 0, 11.5, 17)
        self.customer4 = Customer(3, 11, 11.5, 20)
        self.pub.drinks_list = [self.drink1, self.drink2]
        self.pub.food_list = [self.food1, self.food2]
        self.pub.stock_list =   {
                                "drinks": 
                                {"pint of beer" : 20,
                                "still water" : 100},

                                "food": 
                                {"Pie" : 10,
                                 "sandwich" : 8}
        }
    

    
    
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
        self.pub.sell_drink(self.drink1, self.customer4)
        self.pub.sell_drink(self.drink2, self.customer3)
        self.assertEqual(104.5, self.pub.till)
        self.assertEqual(18, self.customer1.wallet)
        self.assertEqual(11,self.customer4.drunkness)
        self.assertEqual(99 ,self.pub.stock_list["drinks"]["still water"])
        self.assertEqual(19 ,self.pub.stock_list["drinks"]["pint of beer"])

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

    def test_sell_food(self):
        self.pub.sell_food(self.food1, self.customer4)
        self.assertEqual(8, self.customer4.drunkness)
        self.assertEqual(6, self.customer4.wallet)
        self.assertEqual(105.5, self.pub.till)
    
    def test_check_stock(self):
        self.assertEqual(20, self.pub.stock_list["drinks"]["pint of beer"])
        self.assertEqual(10, self.pub.stock_list["food"]["Pie"])

    def test_if_stock_exists(self):
        check1 = "fish"
        check2 = "Pie"
        self.assertEqual(False, self.pub.check_if_stock_exists(check1))
        self.assertEqual(True, self.pub.check_if_stock_exists(check2))
    
    def test_adjust_stock(self):
        self.pub.adjust_stock("Pie", 5)
        self.pub.adjust_stock("pint of beer", -1)
        self.pub.adjust_stock("still water", -1)
        self.assertEqual(15, self.pub.stock_list["food"]["Pie"])
        self.assertEqual(19, self.pub.stock_list["drinks"]["pint of beer"])
        self.assertEqual(99, self.pub.stock_list["drinks"]["still water"])
    
    def test_total_stock_price(self):
        self.assertEqual(177, self.pub.get_total_stock_value())
    
    def test_pub_mark_up(self):
        self.pub.mark_up(1.1)
        self.assertEqual(194.7, self.pub.get_total_stock_value())

