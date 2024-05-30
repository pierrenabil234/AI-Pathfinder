import networkx as nx
import numpy as np
import math as math
def Astar_euclidean(matrix, graph, start, end):
    n = len(matrix)
    Gn_matrix = np.zeros((n, n))
    flag2=0
    for r in range(n):
        for c in range(n):
            if matrix[r][c] == 2:
                rstart=r
                cstart=c
                flag2=1
                Gn_matrix[r][c] = 0
                break
        if flag2 :
            break
                
    
    for r in range(n):
        for c in range(n):
            UC=abs(rstart - r) + abs(cstart - c)
            Gn_matrix[r][c]=UC
    
    Hn_matrix = np.zeros((n, n))

    x, y = 0, 0
    for i in range(n * n):
        min_value = float('inf')
        if matrix[x][y] != 1:
            for r in range(n):
                for c in range(n):
                   if matrix[r][c]==3:
                    X_axis=abs(x-r)**2
                    Y_axis=abs(y-c)**2
                    euclidean_distance=math.floor(math.sqrt(X_axis+Y_axis))
                    if(min_value>euclidean_distance):
                        min_value=euclidean_distance

        Hn_matrix[x][y] = min_value
        if matrix[x][y] == 2:
            HG = min_value
        if x < n - 1:
            x += 1
        else:
            x = 0
            y += 1
    
    print("Hn_matrix:")
    print(Hn_matrix)
    print("greedy matrix:")
    print(Gn_matrix)
    
    visited = []
    fringe = {start: HG}
    parents = {}
    flag=0

    while fringe:
        current = min(fringe, key=fringe.get)
        delete = fringe.pop(current)
      
        if current in visited:
            break

        if current not in visited:
            
            visited.append(current)
            for neighbor in graph[current]:
                nx, ny = neighbor
                if neighbor not in visited:
                    Dis = Hn_matrix[nx][ny]+Gn_matrix[nx][ny]
                    #if Dis < min_val:
                    #   min_val = Dis
                    fringe[neighbor] = Dis  
                    parents[neighbor] = current
        
        for End in end:
                if End == neighbor or End == current :
                    flag=1
                    optimal_path = reconstruct_path(parents, start, End)
                    print(f"optimal_path={optimal_path}")
                    print(f"vis={visited}")
                    return optimal_path,visited
                
        if flag==1:
            break

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
