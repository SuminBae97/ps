import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())




graph = [list(input()) for _ in range(m)]
visited = [[False] * n for i in range(m)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,c):
    q = deque([(x,y)])
    visited[x][y]=True
    count=0
    while q:
        count+=1
        nx,ny = q.popleft()
        for i in range(4):
            px = nx+dx[i]
            py = ny+dy[i]

            if px < 0 or px >= m or py < 0 or py>=n:
                continue
            
            if visited[px][py]==False and graph[px][py]==c:
                q.append([px,py])
                visited[px][py]=True

    return count

answer_w =[]
answer_b =[]
for i in range(m):
    for j in range(n):
        if visited[i][j]==False:
            if graph[i][j]=='W':
                val= bfs(i,j,'W')
                answer_w.append(val)
            else:
                val = bfs(i,j,'B')
                answer_b.append(val)
val_w = 0
val_b = 0

for v in answer_w:
    val_w+=(v)**2

for v in answer_b:
    val_b+=(v)**2
print(val_w,val_b)