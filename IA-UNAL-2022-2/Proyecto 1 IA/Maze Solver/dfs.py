
def dfs(G, start, end):

    visited = [(0,start)]
    cnt = 1

    visited_nodes = [start]

    _dfs(G, start, end, visited, visited_nodes, cnt)


    

    return visited, visited_nodes

def _dfs(G, start, end, visited, visited_nodes, lvl):
    
    

    for n in G.nbrs(start):
        
        if end in visited_nodes:
            break

        if n == end:
            visited.append((lvl, n))
            visited_nodes.append(n)
            break

        if n not in visited_nodes:
            #print(n)
            visited.append( (lvl, n) )
            visited_nodes.append(n)
            _dfs(G, n, end, visited, visited_nodes, lvl+1)





'''
def DFS_Path(G: UndirectedEdgeSetGraph, visited, visited_nodes):

    path = []

    visited_cop = visited
    
    visited_index = []
    for i in visited:
        visited_index.append(i[0])

    
    orderer_visited = []
    
    for i in range(0, max(visited_index)+1):
        
        for j in visited_cop:
            if j[0] == i:
                orderer_visited.append(j)

            
    


    
    

    return path
'''


