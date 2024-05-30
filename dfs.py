import networkx as nx
import random as rn
def DFS(graph, start, end):
    visited = []
    fringe = []
    parents = {}

    visited.append(start)
    fringe.append(start)

    while fringe:
        current = fringe.pop()
        Array_ran=[]
        if not current:
            break
        for neighbor in graph[current]:
            if neighbor not in visited:
                  Array_ran.append(neighbor)
        
        if(Array_ran):
            n=len(Array_ran)
            for i in range (n):
                choose_one= rn.randint(0,(len(Array_ran)-1))
                take=Array_ran[choose_one]
                fringe.append(take)
                x=Array_ran[choose_one]
                Array_ran[choose_one]=Array_ran[len(Array_ran)-1]
                Array_ran[len(Array_ran)-1]=x
                Array_ran.pop()
                parents[take] = current

        for End in end:
            if End == current:
                optimal_path = reconstruct_path(parents, start, End)
                visited.pop(0)
                return visited, optimal_path

        visited.append(current)

    return visited,[]

def reconstruct_path(parents, start, end):
    path = [end]

    while path[-1] != start:
        current = parents[path[-1]]
        path.append(current)
    return path[::-1]

