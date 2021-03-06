from src.food import Food


class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks_list = []
        self.food_list = []
        self.stock = {}

    def add_drink_to_list(self, drink):
        self.drinks_list.append(drink)

    def count_drinks_list(self):
        return len(self.drinks_list)

    def sell_drink(self, drink, customer):
        if (self.check_customer_age(customer) == True and customer.drunkness < 10) or (drink.alcoholic_status == False):
            customer.decrease_wallet(drink.price)
            self.increase_till(drink.price)
            customer.drunkness += drink.alcohol_units
            self.adjust_stock(drink.name, -1)
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

    def sell_food(self, food, customer):
        customer.decrease_wallet(food.price)
        self.increase_till(food.price)
        customer.drunkness -= food.rejuvenation_level
        self.adjust_stock(food, -1)

    def check_if_stock_exists(self, stock):
            if stock in self.stock_list["food"] or stock in self.stock_list["drinks"]:
                return True
            else:
                return False
            
    def adjust_stock(self, stock, amount):
        for key in self.stock_list["food"].keys():
            if key == stock:
                self.stock_list["food"][key] = self.stock_list["food"][key] + amount
        for key in self.stock_list["drinks"].keys():
            if key == stock:
                self.stock_list["drinks"][key] = self.stock_list["drinks"][key] + amount
    
    def get_total_stock_value(self):
        total = 0
        for key in self.stock_list["drinks"]:
            for drink in self.drinks_list:
                if key == drink.name:
                    total += drink.price * self.stock_list["drinks"][drink.name]
        for key in self.stock_list["food"]:
            for food in self.food_list:
                if key == food.name:
                    total += food.price * self.stock_list["food"][food.name]
        return total

    def mark_up(self, mark_up):
            for drink in self.drinks_list:
                drink.price *= mark_up
            for food in self.food_list:
                food.price *= mark_up