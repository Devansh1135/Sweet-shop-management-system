import unittest
from sweet_shop import SweetShop

class TestSweetShop(unittest.TestCase):
    def test_add_sweet(self):
        shop = SweetShop()
        shop.add_sweet(1,"Kaju katli","sweet",900,5)
        sweets = shop.get_all_sweets()
        self.assertEqual(len(sweets),1)
        self.assertEqual(sweets[0].sweet_name,"Kaju katli")
        self.assertEqual(sweets[0].sweet_price_per_kg,900)

    def test_delete_sweet(self):
        shop = SweetShop()
        shop.add_sweet(1,"Kaju Katli","sweet",900,5)
        shop.add_sweet(2,"Gulab jamun","sweet",500,10)
        shop.delete_sweet(1)
        sweets = shop.get_all_sweets()
        self.assertEqual(len(sweets),1)
        self.assertEqual(sweets[0].sweet_id,2)

    def test_search_sweet(self):
        shop = SweetShop()
        shop.add_sweet(1,"Kaju Katli","sweet",900,5)
        result = shop.search_sweet_by_name("Kaju Katli")
        self.assertEqual(result.sweet_id,1)

    def test_search_category(self):
        shop = SweetShop()
        shop.add_sweet(1,"Kaju Katli","sweet",900,5)
        result = shop.search_sweet_by_category("sweet")
        self.assertEqual(result.sweet_id,1)


        
if __name__ == '__main__':
    unittest.main()