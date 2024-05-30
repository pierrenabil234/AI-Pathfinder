#import networkx as nx
#import numpy as np
#def ASTAR(matrix, graph, start, end):
#    n=len(matrix)
#
#    
#    Hn_matrix=np.zeros((n,n))
#
#    x=0
#    y=0
#    for i in range (n*n):
#        min= float('inf')
#        if(matrix[x][y]!=1):
#            for r in range(n):
#                for c in range(n):
#                    if matrix[r][c]==3:
#                        Md=abs(x - r) + abs(y - c)
#                        if(min>Md):
#                            min=Md
#                
#        
#        Hn_matrix[x][y]=min
#        if x < n-1:
#            x+=1
#        else:
#            x=0
#            y+=1
#        
#    
#    visited = []
#    fringe = {start: 0}
#    parents = {}

#    while fringe:
#        current = fringe.pop(0)
#        if len(current) == 0:
#            break
#
#        min_val = float('inf')
#       for neighbor in graph[current]:
#            nx, ny = neighbor
#
#            if neighbor not in visited:
#                Dis = Hn_matrix[nx][ny]
#                
#                if Dis < min_val:
#                    min_val = Dis
#                
#                parents[neighbor] = current
#
#        #visited.append(current)
#
#
#    print(Hn_matrix)
#    print(min_val)
    
    

import networkx as nx
import numpy as np

def ASTAR(matrix, graph, start, end):
    n = len(matrix)

    Hn_matrix = np.zeros((n, n))

    x, y = 0, 0
    for i in range(n * n):
        min_val = float('inf')
        if matrix[x][y] != 1:
            for r in range(n):
                for c in range(n):
                    if matrix[r][c] == 3:
                        Md = abs(x - r) + abs(y - c)
                        if min_val > Md:
                            min_val = Md

        Hn_matrix[x][y] = min_val
        if matrix[x][y] == 2:
            HG=min_val
        if x < n - 1:
            x += 1
        else:
            x = 0
            y += 1
    print("Hn_matrix:")
    print(Hn_matrix)
    
    visited = []
    fringe = {start: HG}
    parents = {}
    flag=0

    while fringe:
        current = min(fringe, key=fringe.get)
        delete = fringe.pop(current)
      
        if current in visited:
            print("saif break")
            break

        if current not in visited:
            
            visited.append(current)
            print("saif append")
        
            for neighbor in graph[current]:
                nx, ny = neighbor
                if neighbor not in visited:
                    Dis = Hn_matrix[nx][ny]
                    #if Dis < min_val:
                    #   min_val = Dis
                    fringe[neighbor] = Dis  
                    parents[neighbor] = current
        
        for End in end:
                if End == neighbor or End == current :
                    print("saif end")
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





