

#%%
class Product:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
class Service:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
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
            if isinstance(item, Product):
                return 0.98 * item.price
            else:
                return item.price
        else:
            return item.price
            
cart = [
        Product("guitar", 1000),
        Product("pick box", 5),
        Service("Insurance", 5),
        Service("Insurance", 5)
        ]

normal_tier = Tier("normal")
silver_tier = Tier("silver")
gold_tier = Tier("gold")


class 

def checkout(shopping_cart, tier=normal_tier): 
    if  shopping_cart == []:
        print("go back shopping!")
        return None
        
    total = 0
    
    services_in_cart = set()
    
    for item in shopping_cart:
        
        if isinstance(item, Service):
            if item.name in services_in_cart:
                continue            
            else:
                services_in_cart.add(item.name)
            
        total += tier.discount(item)
    
    return total
    
    
    
    
    
    
    
    
    
    
    
    
    
    
Press h to open a hovercard with more details.
