class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks_list = []

    def add_drink_to_list(self, drink):
        self.drinks_list.append(drink)

    def count_drinks_list(self):
        return len(self.drinks_list)

    def sell_drink(self, drink, customer):
        customer.decrease_wallet(drink.price)
        self.increase_till(drink.price)

    def increase_till(self, amount):
        self.till += amount
