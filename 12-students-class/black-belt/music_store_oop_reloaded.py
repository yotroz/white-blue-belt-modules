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
    products = []
    services = []
    
    def __init__(self, name):
        self.name = name
#       self.products = []
#       self.services = []

        
    def add_product_to_cart(self, product):
        self.products.append(product)
        return "A $" + str(product.price) + " " + str(product.name) + " has been added to you cart!"
    
    def add_service_to_cart(self, service):
        if service not in self.services: 
            self.services.append(service)
            return "A $ " + str(service.price) + " " + str(service.name) + " has been added to you cart!"
        else: 
            return "This " + str(service.name) + " is already added to you cart!"
        
    def checkout(self, tier): 
        
        final_price = 0
        
        
        for product in self.products:
                if tier == gold or silver:
                    final_price += product.price * tier.discount
                
                else: 
                     final_price += product.price * tier.discount
                
        for service in self.services: 
                print(service)
                if tier == gold:
                    final_price += service.price * tier.discount
            
                else:
                    final_price += service.price 
  
        return final_price
                
 
#We create the tiers    
gold = Tier("gold", .95)  
silver = Tier("silver", .98)
normal = Tier("normal", 1)
platinum = Tier("platinum", .70)



#We create the products
guitar = Product("Guitar", 1000)
pick_box = Product("Pick box", 5)
guitar_string = Product("Guitar string", 10)
bass = Product("Bass", 550)

#We create the services
insurance = Service("Insurance", 5)
priority_mail = Service("Priority mail", 10)



#tests cases 
#cart1 = Cart("Billy's")
#
#cart1.add_product_to_cart(guitar)
#cart1.add_product_to_cart(guitar)
#
#cart1.add_service_to_cart(insurance)
#cart1.add_service_to_cart(insurance)
#cart1.add_service_to_cart(insurance)


#cart2 = Cart("Tommy's")
#
#cart2.add_product_to_cart(guitar)
#cart2.add_product_to_cart(pick_box)
#
#cart2.add_service_to_cart(insurance)
#cart2.add_service_to_cart(priority_mail)
#cart2.add_service_to_cart(priority_mail)
#cart2.add_service_to_cart(priority_mail)







    

