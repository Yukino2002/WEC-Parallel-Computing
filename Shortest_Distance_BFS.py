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


print("Enter the number of nodes: ", end ="")
n = int(input())
print("Enter the number of edges: ", end = "")
e = int(input())
for _ in range(e):
    u, v = map(int, input().split())
    edge(Graph, u, v)

distance = [0] * (n)

BFS(Graph, 0, distance)
print(distance)