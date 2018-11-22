#%%

#Create a function non_connected to find non-connected nodes in a graph

graph =  {
            "a": ["b","c"],
            "b": ["d"],
            "c" : ["d"],
            "d" : ['e'],
            "e": [], 
            "f": []
            }

def non_connected(g): 
    a = []
#    
#    for node in g: 
#        for edge in g[node]:
#           print(len(g[node]))
#           if len(g[node]) == a: 
#               print(node)
##                print(len(g[node])
##    
#    i = 0 
#    
#    for node in g: 
#        if node[i] == a: 
#            print("yes")
#            i+=1
    
    for node in g: 
        if g[node] == a: 
            return "the node '" + node + "' has no edges "

#    for node in g: 
#        for edge[g] in 
#        if node.value() == a:
#            return node.item()
            
        
def non_connected_reloaded(g): 
    
    a = []
    b =[]
    i = 0
    y= 0
    
    nodes_without_edges = []
    
    for node in g: 
        if g[node] == b:
            a.append(node)
            print(a)
            i +=1
#     

    for node in g: 
#        print(g[node])
        if a[y] in g[node]: 
#           return 
            print(g[node][y]  + " is in " +  node)
            y+=1
        else:
            print(g[node][y]  + " is not in " +  node)
            nodes_without_edges.append(node)
            y+=1
        
    return nodes_without_edges
            
#            return a[0] + " Has an edge with " + node 
        
        
#    for node2 in g: 
#        print(g[node2])
#        if a[0] not in g[node2]: 
#            return "the node '" + a[0] + "' has no edges "
#                
#        else: 
#            return "they all have edges"
#            
non_connected_reloaded(graph)

#%%


graph =  {
            "a": ["b","c"],
            "b": ["d"],
            "c" : ["d"],
            "d" : ['e'],
            "e": [], 
            "f": []
            }

def non_connected_try(g): 
    a = []
    b =[]
    i = 0
    y= 0
    
    nodes_without_edges = []
    
    for node in g: 
        if g[node] == b:
            a.append(node)
            print(a)
            i +=1
            
    print("this are my nodes without edges" + str(nodes_without_edges))        
    
    for node in a: 
        print(node)
        counterno = 0 
        for other_node in g:
            if node not in g[other_node]:
                counterno += 1
                print(counterno)
                if counterno == len(g): 
                    return node + " NOT ANYWHERE"
                
                    print(node + " is a reference somewhere")
#                break
#                print("not anywhere")
                
                
                    
#            print(other_node)
#            if node in g[other_node]:
#                print(node + "this one isnt in " + other_node)
#                  
#            elif: 
#            else:   
#                nodes_without_edges.append(node)
#                pass
#                print("this are my nodes without edges" + str(nodes_without_edges)) 
                
    
#    return nodes_without_edges
    
    
    
    
    