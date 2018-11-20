

#%%

from music_store_oop_reloaded import Cart.checkout

def test_normal_all_products_and_services(): 
    value = [["Guitar", "Priority mail", "Pick box", "Guitar string", "Insurance"]]   
        
    for case in value:
        
        assert checkout(case,"normal") == 1030   

def test_gold_all_products_and_services(): 
    value = [["Guitar", "Priority mail", "Pick box", "Guitar string", "Insurance"]]   
        
    for case in value:
        
        assert checkout(case, "gold") == 978.5    
        
def test__silver_all_products_and_services(): 
    value = [["Guitar", "Priority mail", "Pick box", "Guitar string", "Insurance"]]   
        
    for case in value:
        
        assert checkout(case, "silver") == 1009.7      