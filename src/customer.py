class Customer:
    def __init__(self, id, belly, wallet):
        self.id = id
        self.belly = belly
        self.wallet = wallet
    
    def decrease_wallet(self, amount):
        self.wallet -= amount