from collections import deque

def solution(n, computers):
    graph = [[] for _ in range(n+1)]
    visited = [False]*(n+1)
    for i in range(n):
        for j in range(n):
            if i==j:
                pass
            elif computers[i][j]==1:
                graph[i+1].append(j+1)
    def bfs(x):
        q = deque([x])
        visited[x]=True
        while q:
            val = q.popleft()
            for node in graph[val]:
                if visited[node]==False:
                    q.append(node)
                    visited[node]=True
    count = 0
    for i in range(1,n+1):
        if visited[i]==False:
            bfs(i)
            count+=1
    return count