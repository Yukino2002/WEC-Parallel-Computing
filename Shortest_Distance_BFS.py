from collections import defaultdict
import time
Graph = defaultdict(list)

def edge(Graph, u, v):
    Graph[u].append(v)
    Graph[v].append(u)

def BFS(Graph, s, distance, n):
    
    visited = [False] * (n)

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


n, e = map(int, input().split())
for _ in range(e):
    u, v = map(int, input().split())
    edge(Graph, u, v)

distance = [0] * (n)

st = time.time()

BFS(Graph, 0, distance, n)
print(*distance)

ed = time.time()
print(ed - st)