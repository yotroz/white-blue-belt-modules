#%%
from itertools import combinations

graph10 =  {
            "a": ["b","c","d"],
            "b": ["d"],
            "c" : ["a"],
            "d" : ["a"],
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
    
#    problem this still doesn't work if we repeat connections
    
    nodes = [nodes for nodes in graph]    
    
    combinations_list = list(combinations(nodes,2))
    
    combinations_clean = [''.join(element) for element in combinations_list]
      
    edges = [node + other_node for node in graph for other_node in graph[node]]    

    counter = 0
    for edge in edges: 
        if edge in combinations_clean or edge[::-1] in combinations_clean:
            counter += 1
            if counter == len(combinations_clean): 
                return "THE GRAPH IS TOTALLY FOOOKING CONNECTED"

    return "FOOOK NO!! THE GRAPH IS NOT TOTALLY CONNECTED"
                






#%%
from itertools import combinations, permutations

#Writting our own combinations algorithm could probably take a while: 
# The actual implementation of the combinations function from the library 
# is quite long: 
#https://docs.python.org/2/library/itertools.html#itertools.combinations

graph1 =  {
            "a": ["b","c","d"],
            "b": ["d"],
            "c" : ["d"],
            "d" : ["a"],
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
        
graph10 =  {
            "a": ["b","c","d"],
            "b": ["d"],
            "c" : ["d"],
            "d" : ["a"],
            }


def fully_connected_explanation(graph):  
    
#    Explanation 
#    STEP 1: 
#    we get the nodes of our graph
    
    nodes = [nodes for nodes in graph]    
    
#    STEP 2:
#    we get the combinations with a library. These are the necessary 
#    connections two achieve a fully connected graph. We use combinations and
#    not permutations because we consider 'ab' to be equal to 'ba'
    
    combinations_list = list(combinations(nodes,2))
    
    
#    STEP 3: 
#    we convert the combinations tuplets into a list of two-character strings.
#    We use a list comprehension but it's the same as the follwing code:
#    
#    combinations_clean = []
#    
#    for element in combinations_list: 
#         combinations_clean.append(''.join(element))
         
   
    
    
    combinations_clean = [''.join(element) for element in combinations_list]
 
#    STEP 4
#    We get the edges of our graph in the same format as our combinations. 
#   We use a list comprehension but it's the same as the follwing code:
    
#     edges = []   
#     for node in graph: 
#        for other_node in graph[node]: 
#            edges.append(node + other_node)
     
    edges = [node + other_node for node in graph for other_node in graph[node]]    


 
#    STEP 5: The magic
    counter = 0
    for edge in edges: 
        if edge in combinations_clean or edge[::-1] in combinations_clean:
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

def fully_connected_node(g): 
    
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
            
    
    return "The nodes '" + str(connected_nodes) + "' are connected to all nodes"


#%%
            
from itertools import combinations, permutations
        
graph1 =  {
            "a": ["b","c","d","e", "d"],
            "b": ["d"],
            "c" : ["d"],
            "d" : ["e"],
            }

def fully_connected_permutations(graph): 
    
        
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
    


    
          
