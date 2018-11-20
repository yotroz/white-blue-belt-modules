#Migrate the music store program we created to an OOP approach. 
#You can use classes for modelling products, services, customer tier, 
#the shopping cart...
#
#Products have name and price.
#Services have price.
#Customer tier have a discount.
#Shopping cart has:
#a list of products
#a list of services
#and a method to add new products and another for services
#a checkout method that receives a customer tier and calculates the price# 

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
    def __init__(self, name, discount):
        self.name = name
        self.discount = discount 

class Cart: 
    def __init__(self, products, services):
        self.products = []
        self.services = []
        
    def add_product_to_cart(self, product):
        self.products.append(product)
    
    def add_service_to_cart(self, service):
        if service not in self.services: 
            self.services.append(service)
        else: 
            pass
        
    def checkout(self, tier): 
        for product in self.products:
            if tier == "gold":
                return (product.price + service.price)* self.tier.discount
            
            elif tier == "silver":
                return (self.products.price * tier.discount) + self.services.price
            
            else: 
                return self.products.price + self.services.price
            
gold = Tier("gold", .95)  

silver = Tier("silver", .98)

guitar = Product("Guitar", 1000)

pick_box = Product("Pick box", 5)

guitar_string = Product("Guitar string", 10)

insurance = Service("Insurance", 5)

priority_mail = Service("Priority mail", 10)

test_cart = Cart("Guitar", "Insurance")

test_cart.add_product_to_cart(guitar)




    

