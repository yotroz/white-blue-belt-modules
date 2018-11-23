#%%

from blue_belt import fully_connected

def test_six_edges_but_one_repeated(): 
    
    value = [
                {
                "a": ["b","c"],
                "b": ["c"],
                "c": ["b", "d"],
                "d": ["b"],
                }, 
                        
                {
                "a": ["d"],
                "b": ["c", "d", "a"],
                "c": ["a"],
                "d": ["a"],
                },                         
            
                
            ]
    
    for case in value:
        
        assert fully_connected(case) == "FOOOK NO!! THE GRAPH IS NOT TOTALLY CONNECTED"



