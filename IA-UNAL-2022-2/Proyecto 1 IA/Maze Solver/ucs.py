
# UNIFORM COST  SEARCH ALGORITHM
# Suposse each path between nodes has value 1.

# Build an associated tree to graph



from collections import deque
from graph import UndirectedEdgeSetGraph


# =========== PATHS FROM TREE


# Get all path of tree

paths = []

def printRootToLeafPaths(G: UndirectedEdgeSetGraph, node: str, path: deque):

    children_list = G.children(node)
    for i in path:
        
        if children_list.count(i) > 0:
            children_list.remove(i)
    

    if node == '' or node is None:
        return
 
    path.append(node)
    
    if len(children_list)==0:
        curr_path = tuple(path)
        paths.append(curr_path)
        #print(curr_path)

    for child in children_list:
        printRootToLeafPaths(G, child, path)

    
    path.pop()
 


def printRootToLeafPath(G, root):
 
    path = deque()
    #paths = []

    
    printRootToLeafPaths(G, root, path)

def ucs(G, start, end):

    printRootToLeafPath(G, start)

    all_paths_to_end = []
   
    for path in paths:
        
        if path.count(end)>0:
            all_paths_to_end.append( path[0:path.index(end)+1] )
    
    low_cost_path = all_paths_to_end[0]

    for path_end in all_paths_to_end:
        if len(path_end) < len(low_cost_path):
            low_cost_path = path_end

    #paths.remove(low_cost_path)
    #paths.append(low_cost_path)
    

    return all_paths_to_end, low_cost_path

