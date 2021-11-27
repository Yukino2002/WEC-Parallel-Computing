import multiprocessing
from collections import defaultdict
import time

# Graph declared as list of lists
Graph = defaultdict(list)
Visited = []
Distance = []

# Edge function to append the lists of all individual nodes
def Edge(u, v):
    Graph[u].append(v)
    Graph[v].append(u)

# The Neighbours function returns the nearby neighbours of the vertex passed in it
# It only appends those neighbouring vertices which have a visited truth value of false
# or have not been visited yet
def Neighbours(node):
    Graph[node]
    neighbour = []
    for nodes in Graph[node]:
        if Visited[nodes] == False:
            neighbour.append(nodes)
            Visited[nodes] = True
            Distance[nodes] = Distance[node] + 1
    
    return neighbour


# The BFS function is used to compute the shortest distance parallely
# What we are trying to do is, for every node, we check it's unvisited neighbours
# We are using multiprocessing for checking the number of unvisited neighbours and appending them
# .Pool() is used for execution of a function across multiple input values parallely 
# We get a list of unvisited neighbours, for whom we check again, this time we get a list of lists
# We convert the list of lists into a list and again repeat the process
def BFS_Multiprocessing(level):
    
    while(len(level)):
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
    n, e = map(int, input().split())

    # initialsing these as .Array() so that the data can be shared among different processes
    Distance = multiprocessing.Array('i', n)
    Visited = multiprocessing.Array('i', n)

    for _ in range(e):
        u, v = map(int, input().split())
        Edge(u, v)

    st = time.time()

    Visited[0] = True
    BFS_Multiprocessing([0])
    print(*Distance[:])
    
    ed = time.time()
    print(ed - st)
