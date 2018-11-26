#%%
graph = {
     "a": ["b", "c"],
     "b": ["d"],
     "c": ["d"],
     "d": [],
     "e": []
     }

def non_connected(g):
    
    non_connected_nodes = []
    
    outgoing_edges = []
    
    for node in g:
        for outgoing_edge in g[node]:
            outgoing_edges.append(outgoing_edge)
    
    for node in g:
        if g[node] == [] and node not in outgoing_edges:
            non_connected_nodes.append(node)
    
    
    return non_connected_nodes

#%%
    
graph = {
        "a": ["b", "c"],
        "b": ["c", "a"],
        "c": ["a", "b"]
        }

def fully_connected(g):
    nodes = len(list(g.keys()))
    edges = []
    
    for node in g:
        for edge in g[node]:
            edges.append(edge)
            
    return len(edges) == nodes * (nodes - 1)





