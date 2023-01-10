import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
graph = []
visited = [[False]*(m) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]


for _ in range(n):
    tmp = list(map(int,sys.stdin.readline().split()))
    graph.append(tmp)

dest_loc = None
for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            dest_loc = [i,j]
            break


ans = [[-1]*(m) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            ans[i][j]=0


def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y]=True

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue

            if graph[nx][ny]==1 and visited[nx][ny]==False:
                ans[nx][ny] = ans[x][y]+1
                visited[nx][ny]=True
                q.append([nx,ny])
ans[dest_loc[0]][dest_loc[1]] = 0
bfs(dest_loc[0],dest_loc[1])


for i in range(n):
    for j in range(m):
        print(ans[i][j],end=' ')
    print()