from collections import defaultdict
from collections import deque
import multiprocessing as mp
from multiprocessing import process
import multiprocessing


graph = defaultdict(list)
visited = []
numberOfVertices = 5
numberOfEdges = 5
distance = []
q = deque()

def addNeighbours(parent):
    visited[parent] = True
    neighbours = []
    for node in graph[parent]:
        if not visited[node]:
            neighbours.append(node)
            visited[node] = True
            distance[node] = distance[parent] + 1

    return neighbours    



def addEdge(u, v):    
    graph[u].append(v)   
    graph[v].append(u)


# def bfs(source):    
#     q = deque([source])   
#     visited = [0] * numberOfVertices
#     distance[source] = 0
#     while q:
#         front = q.popleft()
#         print(front)
#         for node in graph[front]:
#             if not visited[node]:
#                 visited[node] = 1
#                 distance[node] = distance[front] + 1
#                 q.append(node)
    
        
def parallelBFS(level):

    while(level) :    
        # print(level)
        newLevel = []
        cpu_count = mp.cpu_count()
        pool = mp.Pool(processes = cpu_count)
        newLevel = pool.map(addNeighbours, [node for node in level])
        flatNewLevel = []
        for lst in newLevel:
            for node in lst:
                flatNewLevel.append(node)   
        level = flatNewLevel



if __name__ == '__main__':
    
    numberOfVertices, numberOfEdges = map(int, input().split())
    
    visited = multiprocessing.Array('i', numberOfVertices)
    distance = multiprocessing.Array('i', numberOfVertices)
    for _ in range(numberOfEdges):
        x, y  = map(int, input().split())
        addEdge(x, y)

    parallelBFS([0])
    
    print(*distance[:])
