##########part 1 ##########
import heapq

def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def A_star(maze, start, goal, n, m):
    sx, sy = start
    ex, ey = goal

    visited = [[False for j in range(m)] for i in range(n)]
    heap = []
    
    heapq.heappush(heap, (manhattan(sx, sy, ex, ey), 0, sx, sy, ""))

    while heap:
        f, cost, x, y, path = heapq.heappop(heap)

        if visited[x][y]:
            continue
        visited[x][y] = True

        if (x, y) == (ex, ey):
            print(cost)
            print(path)
            return

        if x - 1 >= 0 and maze[x-1][y] == '0' and not visited[x-1][y]:
            h = manhattan(x-1, y, ex, ey)
            heapq.heappush(heap, (cost + 1 + h, cost + 1, x - 1, y, path + 'U'))

        if x + 1 < n and maze[x+1][y] == '0' and not visited[x+1][y]:
            h = manhattan(x+1, y, ex, ey)
            heapq.heappush(heap, (cost + 1 + h, cost + 1, x + 1, y, path + 'D'))

        if y - 1 >= 0 and maze[x][y-1] == '0' and not visited[x][y-1]:
            h = manhattan(x, y-1, ex, ey)
            heapq.heappush(heap, (cost + 1 + h, cost + 1, x, y - 1, path + 'L'))

        if y + 1 < m and maze[x][y+1] == '0' and not visited[x][y+1]:
            h = manhattan(x, y+1, ex, ey)
            heapq.heappush(heap, (cost + 1 + h, cost + 1, x, y + 1, path + 'R'))

    print(-1)



n, m = map(int, input().split())
sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
maze = [list(input().strip()) for i in range(n)]
A_star(maze, (sx, sy), (ex, ey), n, m)

############ Part 2 ############
'''from collections import deque

def admissible(n, m, a, b, graph):
   
    
    queue=[]
    visited=[False]*(n+1)
    distance=[0]*(n+1)
    visited[b]=True
    queue.append(b)
    
    while queue:
        current=queue.pop(0)
        current_distance=distance[current]
        for i in graph[current]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                distance[i]=current_distance+1
    return distance


n, m = map(int, input().split())
a, b = map(int, input().split())

heuristics = [0] * (n + 1)
for i in range(n):
    x, y = map(int, input().split())
    heuristics[x] = y

edges = []
for i in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))
graph = [[] for i in range(n + 1)]
for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
actual_cost=admissible(n,m,a,b,graph)
inadmissible_list=[]
for i in range(len( heuristics)):
    if  heuristics[i]!=actual_cost[i]:
        inadmissible_list.append(i)
if len(inadmissible_list)==0:
    print(1)
else:
    print(0)
    
    print(f"Here nodes {','.join(map(str,inadmissible_list))} are inadmissible")'''

