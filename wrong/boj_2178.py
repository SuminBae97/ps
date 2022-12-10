import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

graph = [list(map(int,input())) for _ in range(n)]
visited = [[False]*(m) for _ in range(n)]

dx = [1, -1, 0, 0] 
dy = [0, 0, 1, -1]


def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y]=True

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue

            if graph[nx][ny]==1 and visited[nx][ny]==False:
                graph[nx][ny] = graph[x][y]+1
                q.append((nx,ny))
                visited[nx][ny]=True

bfs(0,0) 
print(graph[n-1][m-1])
