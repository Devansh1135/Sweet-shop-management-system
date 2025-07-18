from sweet import Sweet

class SweetShop:
    def __init__(self):
        self.sweets = []

    def add_sweet(self, id,name,category,price,quantity):
        if self.search_sweet_by_id(id):
            raise ValueError(f"sweet with id {id} already exists !")
        sweet = Sweet(id,name,category,price,quantity)
        self.sweets.append(sweet)

    def delete_sweet(self, id):
        for sweet in self.sweets:
            if sweet.sweet_id == id:
                self.sweets.remove(sweet)
                return True
        return False
    
    def search_sweet_by_id(self,id):
        for sweet in self.sweets:
            if sweet.sweet_id == id:
                return sweet
        return None
    
    def search_sweet_by_name(self,name):
        for sweet in self.sweets:
            if sweet.sweet_name == name:
                return sweet
        return None
    
    def search_sweet_by_category(self,category):
        for sweet in self.sweets:
            if sweet.sweet_category == category:
                return sweet
        return None
    
    def sort_sweets_by_price(self, reverse = False):
        if reverse == False:
            return sorted(self.sweets , key = lambda sweet: sweet.sweet_price_per_kg)
        elif reverse == True:
            return sorted(self.sweets , key = lambda sweet: sweet.sweet_price_per_kg ,reverse=True)
        return None
    
    def purchase_sweet(self, id, quantity):
        sweet = self.search_sweet_by_id(id)
        if not sweet:
            raise ValueError("Sweet not found")

        if sweet.sweet_in_stock < quantity :
            raise ValueError("Not enough sweets in stock")
        
        sweet.sweet_in_stock -= quantity

    def restock_sweet(self,id,quantity):
        sweet = self.search_sweet_by_id(id)
        if not sweet:
            raise ValueError("Sweet not found")
        
        sweet.sweet_in_stock += quantity
        

    def get_all_sweets(self):
        return self.sweets
    