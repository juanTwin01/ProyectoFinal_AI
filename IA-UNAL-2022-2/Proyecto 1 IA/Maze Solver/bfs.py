queue = []  #Initialize a queue


def bfs(G, start, end):

    visited_nodes = [start]

    _bfs(G, start, end, visited_nodes)

    

    return visited_nodes


def _bfs(G, start, end, visited_nodes):  #function for BFS
    queue.append(start)
    for n in G.nbrs(start):
        while queue:  # Creating loop to visit each node
            m = queue.pop(0)
            #print(m, end=" ")
        if end in visited_nodes:
            break

        if n == end:
            visited_nodes.append(n)
            break

        if n not in visited_nodes:
            visited_nodes.append(n)
            _bfs(G, n, end, visited_nodes)
            queue.append(n)


