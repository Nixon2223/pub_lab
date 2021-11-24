class Customer:
    def __init__(self, id, drunkness, wallet, age):
        self.id = id
        self.drunkness = drunkness
        self.wallet = wallet
        self.age = age
    
    def decrease_wallet(self, amount):
        self.wallet -= amount

    def increase_drunkness(self, amount):
        self.drunkness += amount