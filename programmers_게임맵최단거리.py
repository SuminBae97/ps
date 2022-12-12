from collections import deque
def solution(graph):
    
    n = len(graph)
    m = len(graph[0])

    visited = [[False]*(m) for _ in range(n)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]


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
                    q.append([nx,ny])
                    visited[nx][ny]=True
                    graph[nx][ny] = graph[x][y]+1

    bfs(0,0)

    if graph[n-1][m-1]==1:
        return -1
    
    else:   
        return graph[n-1][m-1]