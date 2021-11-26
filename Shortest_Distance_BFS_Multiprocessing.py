import multiprocessing

from collections import defaultdict
Graph = defaultdict(list)

def edge(Graph, u, v):
    Graph[u].append(v)

def BFS(Graph, s, distance):
    
    visited = [False] * (max(Graph) + 1)

    queue = []
    queue.append(s)
    visited[s] = True

    while queue:
        s = queue.pop(0)

        for vertex in Graph[s]:         

            if visited[vertex] == False:
                queue.append(vertex)
                distance[vertex] = distance[s] + 1
                visited[vertex] = True


edge(Graph, 0, 1)
edge(Graph, 0, 2)
edge(Graph, 1, 2)
edge(Graph, 2, 0)
edge(Graph, 2, 3)
edge(Graph, 3, 3)

distance = [0 for _ in range(4)]
BFS(Graph, 2, distance)
print(distance)
