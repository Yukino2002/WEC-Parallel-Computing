import multiprocessing
from collections import defaultdict

Graph = defaultdict(list)

def Edge(u, v):
    Graph[u].append(v)
    Graph[v].append(u)

def Neighbours(node):
    neighbour = []
    for nodes in Graph[node]:
        if Visited[nodes] is False:
            neighbour.append(nodes)
            Visited[nodes] = True
            Distance[nodes] = Distance[node] + 1
    
    return neighbour

def BFS(level):
    

    while(level):
        next_level = []
        cpu = multiprocessing.cpu_count()
        pool = multiprocessing.Pool(processes = cpu)
        next_level = pool.map(Neighbours, [node for node in level])
        flat_level = []
        for lst in next_level:
            for node in lst:
                flat_level.append(node)   
        level = flat_level


if __name__ == '__main__':

    print("Enter the number of nodes: ", end = "")
    n = int(input())
    print("Enter the number of edges: ", end = "")
    e = int(input())

    for _ in range(e):
        u, v = map(int, input().split())
        Edge(u, v)

    Distance = multiprocessing.Array('i', n)
    Visited = multiprocessing.Array('i', n)
    
    Visited[0] = True

    BFS([0])
    print(*Distance[:])
