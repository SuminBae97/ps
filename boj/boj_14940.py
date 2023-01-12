import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
graph =[]
dx = [1,-1,0,0]
dy = [0,0,1,-1]


for _ in range(n):
    tmp = list(map(int,sys.stdin.readline().split()))
    graph.append(tmp)

answer = [[-1]*(m) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
start_x = 0
start_y = 0

for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            start_x = i
            start_y = j
            answer[i][j]=0
        elif graph[i][j]==0:
            answer[i][j]=0


def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y]=True
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue

            if graph[nx][ny]==1 and visited[nx][ny]==False:
                q.append([nx,ny])
                answer[nx][ny] = answer[x][y]+1
                visited[nx][ny]=True

bfs(start_x,start_y)

for i in range(n):
    for j in range(m):
        print(answer[i][j],end=' ')
    print()




