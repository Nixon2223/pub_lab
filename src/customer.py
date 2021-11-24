class Customer:
    def __init__(self, id, belly, wallet,age):
        self.id = id
        self.belly = belly
        self.wallet = wallet
        self.age = age
    
    def decrease_wallet(self, amount):
        self.wallet -= amount