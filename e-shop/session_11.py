#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 13:37:29 2018

@author: yotroz
"""

#%%
#White Belt

"""Our e-shop sells the following products:

   1. Guitar: $1000
   2. Pick box: $5
   3. Guitar Strings: $10

   Create a function named checkout that takes a list that represents a shopping cart and returns the total cost of it.  This function should check that the shopping cart must not be empty.

   Create also some tests for the function.  Try to think of the corner cases.

   Hint: you can represent a product as a dictionary with a name and a price"""

 
#%%
   
product_list = {
        "Guitar": 1000, 
        "Pick box": 5, 
        "Guitar string": 10
        }   
   

#guitar = {
#        product: "Guitar", 
#      price: 1000
#   }

shopping_cart = ["Guitar", "Pick box", "Pick box"]

def checkout(shopping_cart): 
    
    final_price = 0 
    
    if shopping_cart == []:
        return None
    
    else:
        
        for item in shopping_cart: 
            
            final_price += (product_list[item])
            
        
    return final_price
#%%
#Blue Belt     

product_list = {
        "Guitar": 1000, 
        "Pick box": 5, 
        "Guitar string": 10, 
        "Insurance": 5, 
        "Priority mail": 10
        }   


shopping_cart = ["Guitar", "Insurance", "Insurance", "Priority mail", "Priority mail"]

def checkout_2(shopping_cart): 
    
    final_price = 0 
    
    indexes_insurance = [i for i, x in enumerate(shopping_cart) if x == "Insurance"]
    
    
    
    indexes_priority = [b for b, y in enumerate(shopping_cart) if y == "Priority mail"]
    
    if len(indexes_insurance) > 0: 
        final_price += (product_list["Insurance"])
        
    
       
    if len(indexes_priority) > 0: 
        final_price += (product_list["Priority mail"])     
        
        
    
    if shopping_cart == []:
        return None
    
    else:
        
        for item in shopping_cart: 
            if item == "Insurance":
                continue
            
            elif item == "Priority mail": 
                continue
            
            else: 
                final_price += (product_list[item])
            
        
    return final_price


#%%
    
#Black belt 
    


product_list = {
        "Guitar": 1000, 
        "Pick box": 5, 
        "Guitar string": 10, 
        "Insurance": 5, 
        "Priority mail": 10
        }   


shopping_cart = ["Guitar", "Insurance", "Insurance", "Priority mail", "Priority mail"]

tiers = {"normal": 1, 
        "silver": .98,
        "gold": .95 }
    
def checkout_3(shopping_cart, tier): 
    
    final_price = 0 
    
    indexes_insurance = [i for i, x in enumerate(shopping_cart) if x == "Insurance"]
    
    
    
    indexes_priority = [b for b, y in enumerate(shopping_cart) if y == "Priority mail"]
    
    if len(indexes_insurance) > 0: 
        if tier == "gold":
            final_price += (product_list["Insurance"]) * tiers["gold"]
            
        else: 
            final_price += (product_list["Insurance"])
        
    
       
    if len(indexes_priority) > 0: 
        if tier == "gold":
            final_price += (product_list["Priority mail"]) * tiers["gold"]
            
        else: 
            final_price += (product_list["Priority mail"])     
        
        
    
    if shopping_cart == []:
        return None
    
    else:
        
        for item in shopping_cart: 
            if item == "Insurance":
                continue
            
            elif item == "Priority mail": 
                continue
            
            else: 
                final_price += (product_list[item]) * tiers[tier]
            
        
    return round(final_price, 2)  
   








    