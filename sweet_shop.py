from sweet import Sweet

class SweetShop:
    def __init__(self):
        self.sweets = []

    def add_sweet(self, id,name,category,price,quantity):
        sweet = Sweet(id,name,category,price,quantity)
        self.sweets.append(sweet)

    def delete_sweet(self, id):
        for sweet in self.sweets:
            if sweet.sweet_id == id:
                self.sweets.remove(sweet)
                return True
        return False
    
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

    def get_all_sweets(self):
        return self.sweets
    