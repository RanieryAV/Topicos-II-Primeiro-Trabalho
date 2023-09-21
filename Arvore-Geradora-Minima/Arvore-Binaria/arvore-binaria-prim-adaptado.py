import heapq

def prim_mst_binary(graph):
    num_vertices = len(graph)
    
    # Inicialize a árvore geradora mínima como um grafo vazio
    mst = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
    
    # Lista para rastrear os vértices já incluídos na árvore geradora mínima
    included = [False] * num_vertices
    
    # Inicialize a árvore geradora mínima com o primeiro vértice
    included[0] = True
    
    # Variável para contar o número de arestas incluídas na árvore geradora mínima
    num_included = 1
    
    while num_included < num_vertices:
        min_weight = float('inf')
        u, v = None, None
        
        # Encontre a aresta de menor peso que liga um vértice incluído a um vértice não incluído
        for i in range(num_vertices):
            if included[i]:
                for j in range(num_vertices):
                    if not included[j] and graph[i][j] < min_weight:
                        min_weight = graph[i][j]
                        u, v = i, j
        
        # Inclua a aresta na árvore geradora mínima
        mst[u][v] = min_weight
        mst[v][u] = min_weight
        included[v] = True
        num_included += 1
    
    return mst

# Exemplo de uso:
graph = [
    [0, 2, 3, 4],
    [2, 0, 5, 6],
    [3, 5, 0, 7],
    [4, 6, 7, 0]
]

mst = prim_mst_binary(graph)
for row in mst:
    print(row)
