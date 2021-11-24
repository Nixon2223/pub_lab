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
        if self.check_customer_age(customer) == True and customer.drunkness < 10:
            customer.decrease_wallet(drink.price)
            self.increase_till(drink.price)
            customer.drunkness += drink.alcohol_units
        else:
            return f"Please choose a soft drink: {(self.soft_drinks_list())}"

    def increase_till(self, amount):
        self.till += amount
    
    def check_customer_age(self, customer):
        if customer.age >= 18:
            return True
        else:
            return False

    def soft_drinks_list(self):
        soft_drinks = []
        for drink in self.drinks_list:
            if drink.alcoholic_status == False:
                soft_drinks.append(drink.name)
        return soft_drinks

    
    
