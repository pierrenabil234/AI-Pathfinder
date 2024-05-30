
import networkx as nx

def BFS(graph, start, end):
    visited = []
    queue = []
    parents = {}
    # print(f"start {start}")
    visited.append(start)
    queue.append(start)
    # print(graph.edges(start))
    #print(f"Start={start}")
    #print(f"Graph[start]={graph[start]}")  
   # print(f"end={end}")
    while queue:
        current = queue.pop(0)
        if len(current)==0:
            break
        for neighbor in graph[current]:
            
            if neighbor not in visited:
                #print(neighbor)
                visited.append(neighbor)
                queue.append(neighbor)
                parents[neighbor] = current#parents di dictionary by7ot fiha el current node wel neighbour da key
                #fa law 3ndk graph mn a--> b hayb2a parents[b]=a
            for e in end:
                if e == neighbor:
                    #print(f"Goal found at {neighbor}")
                    #print("***********************")
                    #print(f"visited list={visited}")
                    #print(matrix)
                    optimal_path = reconstruct_path(parents, start, e)
                    print(f"optimal_path={optimal_path}")
                    print(f"vis={visited}")
                    return optimal_path,visited              
    return [],visited
def reconstruct_path(parents, start, end):
    path = [end]#hanbd2 mn el end we nro7 el goal 

    while path[-1] != start:#el loop hayb2 mn el last element l7d ma ywsl lel start node
        current = parents[path[-1]]#by7ot fel current el last node mn el dictionary parents
        path.append(current)
    #print(f"optimal path ={path[::-1]}")#print in reversed order
    if len(path)>0:
     return path[::-1]
    else:
        return[]
