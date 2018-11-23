
#%%
from itertools import combinations

graph10 =  {
            "a": ["b","c"],
            "b": ["c"],
            "c" : ["b", "d"],
            "d" : ["b"],
            }

graph2 = {
        "a": ["b", "c", "d"], 
        "b": ["c"], 
        "c": [], 
        "d": ["c"]
               }
        
graph3 = {
        "a": [],
        "b": ["c", "d", "a"], 
        "c": ["d", "a"], 
        "d": ["a"]
        }        
        
 

def fully_connected(graph):  
       
    nodes = [nodes for nodes in graph]    
    
    combinations_list = list(combinations(nodes,2))
    
    combinations_clean = [''.join(element) for element in combinations_list]
      
    edges = [node + other_node for node in graph for other_node in graph[node]]   
    
    counter = 0
    for combination in combinations_clean: 
        if combination in edges or combination[::-1] in edges: 
            counter += 1
            if counter == len(combinations_clean): 
                return "THE GRAPH IS TOTALLY FOOOKING CONNECTED"

    return "FOOOK NO!! THE GRAPH IS NOT TOTALLY CONNECTED"
                            




    
          
