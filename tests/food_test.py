import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food

class TestFood(unittest.TestCase):
    
    def setUp(self):
        self.food = Food("Pie", 5.50, 3)