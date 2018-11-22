#%%


class Company:
    pass

class Worker: 
#    *note the manager=None synthax in the 
#    arguments of the constructor, which means that it has a default value. 
    
    def __init__(self, name, position, manager=None): 
        self.name = name
        self.position = position
        self.manager = manager


    def escalate_complain(self, complaint): 
        if self.manager is not None: 
            self.manager.escalate_complain(complaint)
        else:
            print("I feel your paing about: " + complaint)
        
#we created a ceo position and the we refer it to 
ceo = Worker("Anthony", "CEO")
cto = Worker("Peter", "CTO", ceo)
ctto = Worker("Me", "ctto", cto)

#This following wouldn't work because the method calls the escalate_complain 
#of the manager. The ceo, in this case, does not have  manager:  

    # cto.escalate_complain("I need more toilet paper")
  
    
#To correct this, we simply add an if statement in 17-21 lines. 
# Now it should work
    
#ctto.escalate_complain("I need more toilet paper")
    
#%%

#To model a graph we use dictionaries, where the keys are the nodes and the 
#values are the edges. 
    
#So the one below would read "a is a graph that points to b and c   

graph = {
        "a": ["b", "c"], 
        "b": ["d"],
        "c": ["d"], 
        "d": ["e"], 
        "e": []
        
        }    

#create a function that takes graph as a parameter and returns all the nodes
#in a list 

#my trys
def get_all_nodes(g): 
    
        nodes = [nodes for nodes in g]
        
        return nodes


#def get_all_edges(g):
#    
#    nodes = [nodes for nodes in g]
#    
#    edges =[]
#    i = 0 
#    while i > len(nodes): 
#        edges.append(nodes[i])
#        i+= 1
#        
#    print(edges)    
#    print(nodes[0].key)
#        
##    for node in nodes: 
##        for edge in edges: 
##            print(node[edge])    

    
#pepes solutions
        
def get_all_nodes_pp(g): 
    nodes = []
    
    for node in g: 
        nodes.append(node)
    return nodes

def get_all_edges_pp(g):
    
    edges = []
    
    for node in g: 
        for other_node in g[node]: 
            edges.append(node + " --> " + other_node)
        
    return edges


#def get_all_edges_new(g): 
#    
#    edges = [node for node in g]
#    other_node = [other_node for other_node in g]
#    
#    return str(edges) + " --> " + str(other_node)



    
#%%

    