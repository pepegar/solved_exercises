
#%%
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Item(Product):
    pass
        
class Service(Product):
    pass
        
class Tier:
    
    def __init__(self, name):
        self.name = name
        
    def discount(self, item):
        """
        returns the price...
        """
        if self.name == "gold":
            return 0.95 * item.price
        elif self.name == "silver":
            if isinstance(item, Item):
                return 0.98 * item.price
            else:
                return item.price
        else:
            return item.price
            
cart = [
        Item("guitar", 1000),
        Item("pick box", 5),
        Service("Insurance", 5),
        Service("Insurance", 5)
        ]

normal_tier = Tier("normal")
silver_tier = Tier("silver")
gold_tier = Tier("gold")


class ServiceDuplicatedException(Exception):
    pass

def checkout(shopping_cart, tier=normal_tier): 
    if  shopping_cart == []:
        print("go back shopping!")
        return None
        
    total = 0
    
    services_in_cart = set()
    
    for item in shopping_cart:
        
        if isinstance(item, Service):
            if item.name in services_in_cart:
                raise ServiceDuplicatedException("services can be purchased only once")            
            else:
                services_in_cart.add(item.name)
            
        total += tier.discount(item)
    
    return total
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
