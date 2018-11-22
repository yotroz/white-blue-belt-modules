#%%

#Create a function fully_connected to that returns 
#True if a graph is fully connected, False otherwise

graph1 =  {
            "a": ["b","c","d","e", "d"],
            "b": ["d"],
            "c" : ["d"],
            "d" : ["e"],
            "e": []
            }

def fully_connected(g): 
    
    #this method only works with 
    
#    get the lenght of the nodes
#    evaluate if the current node's edge list has the same lenght as itseñf
#    but first we need to set() the list so we don't get repeated values
#    
    pairs = (len(g) -1)
    
#    print(pairs)
    
    for node in g: 
        if len(set(g[node])) == pairs:
            return "The node '" + node + "' is fully connected"


#%%
            
from itertools import combinations, permutations
        
graph1 =  {
            "a": ["b","c","d","e", "d"],
            "b": ["d"],
            "c" : ["d"],
            "d" : ["e"],
            }

def fully_connected_alt(graph): 
    
        
#   if there is 4 nodes we have to evaluate 6 connections 

#   we need the length of the graph 

    nodes_lenght = len(graph)  
#    
    nodes = [nodes for nodes in graph]
    print(nodes)
    
    
    permutations_list = list(permutations(nodes,2))
    print(list(permutations(nodes,2)))
    
    permutations_clean = []
    
    for element in permutations_list: 
         permutations_clean.append(''.join(element))
#    nodes[0] + 
    print(permutations_clean)
    

            
    i=0
    for node in nodes:  
        
#        print(nodes[i] + nodes[i+1])
#        print(nodes[i] + nodes[i+2])
#        print(nodes[i] + nodes[i+3])
#        print(nodes[i] + nodes[i+4])
        i += 1
#            edges_for_full_connection.append(node+)
        
    
    edges = []
    
    for node in graph: 
        for other_node in graph[node]: 
            edges.append(node + other_node)
#    
            
#    for edge in edges: 
#        if edge in permutations_clean or edge[::-1] in permutations_clean:
            
#       
    print(edges)
    
#%%

graph1 =  {
            "a": ["b","c","d"],
            "b": ["d"],
            "c" : ["d"],
            "d" : ["a"],
            }

graph2 = {
        "a": ["b", "c", "d"], 
        "b": ["c", "d"], 
        "c": []
        
        }

def fully_connected_alt_alt(graph):  
#    
    nodes = [nodes for nodes in graph]
    print(nodes)
    
    
    combinations_list = list(combinations(nodes,2))
    print(combinations_list)
    
    
    combinations_clean = []
    
    for element in combinations_list: 
         combinations_clean.append(''.join(element))
    
    print(combinations_clean)
    edges = []
    
    for node in graph: 
        for other_node in graph[node]: 
            edges.append(node + other_node)
#    
    print(edges)
    
    print(len(combinations_clean))
    
    counter = 0
    for edge in edges: 
        print(edge)
        print(edge[::-1])
        if edge in combinations_clean or edge[::-1] in combinations_clean:
            counter += 1
            if counter == len(combinations_clean): 
                return "THE GRAPH IS TOTALLY FOOOKING CONNECTED"

    return "THE GRAPH IS NOT TOTALLY CONNECTED"
                

    
          
