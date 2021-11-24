import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Tap Water", 0.00, False)

    def test_drink_has_name(self):
        self.assertEqual("Tap Water", self.drink.name)