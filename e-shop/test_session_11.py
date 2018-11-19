#%% WHITE TESTS
from session_11 import checkout 

def test_empty_list_returns_none(): 
    
    value = []
    
    for case in value:
        
        assert checkout(case) == None

def test_list_returns_one_item_price():
    
    value = [["Guitar"]]
    
    for case in value: 
        assert checkout(case) == 1000
        
        
def test_list_returns_two_items_price():
    
    value = [["Guitar", "Pick box"]]
    
    for case in value: 
        assert checkout(case) == 1005      
        
        
        
def test_list_returns_two_same_items_price():
    
    value = [["Guitar", "Guitar"]]
    
    for case in value: 
        assert checkout(case) == 2000         
        
def test_list_returns_item_not_in_list():
    
    value = [["Bass", "Drums"]]
    
    for case in value: 
        assert checkout(case) == 0           
        
        
#%% BLUE TESTS

from session_11 import checkout_2

def test_empty_list(): 
    
    value = []
    
    for case in value:
        
        assert checkout_2(case) == None

def test_repeated_insurance(): 

    value = [["Guitar", "Insurance", "Insurance"]]   
        
    for case in value:
        
        assert checkout_2(case) == 1005
        
def test_repeated_priority(): 

    value = [["Guitar", "Priority mail", "Priority mail"]]   
        
    for case in value:
        
        assert checkout_2(case) == 1010        
         
def test_repeated_both(): 

    value = [["Guitar", "Priority mail", "Priority mail", "Insurance", "Insurance"]]   
        
    for case in value:
        
        assert checkout_2(case) == 1015        
        
def test_all_products_and_services_once(): 

    value = [["Guitar", "Priority mail", "Pick box", "Guitar string", "Insurance"]]   
        
    for case in value:
        
        assert checkout_2(case) == 1030      

def test_two_products_insurance_and_services_once(): 

    value = [["Guitar", "Guitar", "Priority mail", "Pick box", "Guitar string", "Insurance"]]   
        
    for case in value:
        
        assert checkout_2(case) == 2030    
        
def test_two_products_insurance_twice(): 

    value = [["Guitar", "Guitar", "Priority mail", "Pick box", "Guitar string", "Insurance", "Insurance"]]   
        
    for case in value:
        
        assert checkout_2(case) == 2030     

#%%
#Black 

from session_11 import checkout_3

def test_normal_all_products_and_services(): 
    value = [["Guitar", "Priority mail", "Pick box", "Guitar string", "Insurance"]]   
        
    for case in value:
        
        assert checkout_3(case,"normal") == 1030   

def test_gold_all_products_and_services(): 
    value = [["Guitar", "Priority mail", "Pick box", "Guitar string", "Insurance"]]   
        
    for case in value:
        
        assert checkout_3(case, "gold") == 978.5    
        
def test__silver_all_products_and_services(): 
    value = [["Guitar", "Priority mail", "Pick box", "Guitar string", "Insurance"]]   
        
    for case in value:
        
        assert checkout_3(case, "silver") == 1009.7         
            
           