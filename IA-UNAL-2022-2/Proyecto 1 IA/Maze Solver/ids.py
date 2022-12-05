def dfs(G, start, end, limite=9999):

    visited_nodes = [start]

    _dfs(G, start, end, visited_nodes)

    return visited_nodes


def _dfs(G, start, end, visited_nodes, limite=9999):

    for n in G.nbrs(start):

        if end in visited_nodes:
            break

        if n == end:
            visited_nodes.append(n)
            break

        if n not in visited_nodes:

            visited_nodes.append(n)
            _dfs(G, n, end, visited_nodes)


def ids(G, start, end, limite):
    if limite is None:
        return dfs(G, start, end)
    for n in G.nbrs(start):
        for i in range(1, limite + 1):
          resultado = dfs(G, start, end, i)
          if resultado:
              return resultado
