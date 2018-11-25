
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
        
 

def fully_connected_non_directed(graph):  
       
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


#%%

#Create a function fully_connected to that returns 
#True if a graph is fully connected, False otherwise

graph1 =  {
            "a": ["b","c","d","e", "d"],
            "b": ["d"],
            "c" : ["d"],
            "d" : ["a", "b", "c", "e"],
            "e": []
            }

graph2 = {
        "a": ["b", "c"], 
        "b": ["c", "a"], 
        "c": ["b", "a"]
        }

def fully_connected_directed(g): 
    
    #this method only works to find out if a single node is fully connected
    
#    get the lenght of the nodes
#    evaluate if the current node's edge list has the same lenght as itseñf
#    but first we need to set() the list so we don't get repeated values
#    
    pairs = (len(g) -1)
    
#    print(pairs)
    
    connected_nodes = []
    
    for node in g: 
        if len(set(g[node])) == pairs:
            connected_nodes.append(node)
            
    if len(connected_nodes) == pairs + 1: 
        return "The nodes '" + str(connected_nodes) + "' are connected to all nodes. So it is fully connected"

                            




    
          
