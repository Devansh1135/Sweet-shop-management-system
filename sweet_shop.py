from sweet import Sweet

class SweetShop:
    def __init__(self):
        self.sweets = []

    def add_sweet(self, id,name,category,price,quantity):
        sweet = Sweet(id,name,category,price,quantity)
        self.sweets.append(sweet)

    def get_all_sweets(self):
        return self.sweets