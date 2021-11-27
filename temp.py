from collections import defaultdict
import multiprocessing as mp

#Creating a globally accessible graph
graph = defaultdict(list)

#Function to return a list containing all unvisited nodes connected to a parent node
#Used for the pool.map() function
def nextLevel(parent):
    nextLevel = []
    for node in graph[parent]:
        if not visited[node]:
            nextLevel.append(node)
            visited[node] = True
            distance[node] = distance[parent] + 1

    return nextLevel    


#Function to add an edge to the graph
def addEdge(u, v):    
    graph[u].append(v)   
    graph[v].append(u)

# Function for doing BFS paralelly. The idea is simple, until you encounter an empty level, for every
# node in the current level, add its unvisited connected neighbours to a new list (You will get a 
# list of lists). Flatten this list and you obtain the next level. Stop when you encounter an empty level
#(This means that there are no more unvisited nodes in the graph)
def parallelBFS(level):

    while(level) :    
        newLevel = []
        cpu_count = mp.cpu_count()
        pool = mp.Pool(processes = cpu_count)
        newLevel = pool.map(nextLevel, [node for node in level])
        flatNewLevel = []
        for lst in newLevel:
            for node in lst:
                flatNewLevel.append(node)   
        level = flatNewLevel
        pool.close()
        pool.join()



#Runner code

numberOfVertices, numberOfEdges = map(int, input().split())

#Initialising the visited and distance array as multiprocessing Arrays because these can be shared between
# and altered by different processes. 
visited = mp.Array('i', numberOfVertices)
distance = mp.Array('i', numberOfVertices)
visited[0] = True
for _ in range(numberOfEdges):
    x, y  = map(int, input().split())
    addEdge(x, y)

#Starting BFS from the source node as the 0 node
parallelBFS([0])

#Printing the shortest distance of each node from the source node(Including the source node)
for i in range(numberOfVertices):
    print( f"Shortest distance of node {i} from source is {distance[i]}")

