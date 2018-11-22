#%%

#Create a function fully_connected to that returns 
#True if a graph is fully connected, False otherwise

graph =  {
            "a": ["b","c","d","e", "d"],
            "b": ["d"],
            "c" : ["d"],
            "d" : ["e"],
            "e": []
            }

def fully_connected(g): 
    
#    get the lenght of the nodes
#    evaluate if the current node's edge list has the same lenght as itseñf
#    but first we need to set() the list so we don't get repeated values
#    
    pairs = (len(g) -1)
    
#    print(pairs)
    
    for node in g: 
        if len(set(g[node])) == pairs:
            return "The node '" + node + "' is fully connected"

        
        
