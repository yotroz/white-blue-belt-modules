#%%

#Create a function non_connected to find non-connected nodes in a graph


#%%


graph1 =  {
            "a": ["b","c"],
            "b": ["d"],
            "c" : ["d"],
            "d" : ['e'],
            "e": [], 
            "f": [], 
            "g":[]
            }

def non_connected_try(graph): 
    
#    we declare empty lists that we will use to compare later on. 
    
    nodes_with_empty_values = []
    nodes_without_edges = []
    
#    we find all the nodes that comply the first condition: not having a
#    reference in their own values. 
    
    for node in graph: 
        if graph[node] == []:
           nodes_with_empty_values.append(node)
    
#    we compare the nodes with empty values with the values of all of them to 
#    see if there is a value in other nodes. 
    
    for node in nodes_with_empty_values: 
        counterno = 0 
        for other_node in graph:
            if node not in graph[other_node]:
                counterno += 1
                if counterno == len(graph): 
                    nodes_without_edges.append(node)
                    print(node + " has no edges")

    return "This nodes have no edges: " + str(nodes_without_edges)
    
    
    
    
    