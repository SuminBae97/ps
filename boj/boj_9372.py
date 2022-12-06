import sys

def dfs(node,cnt):
    visited[node]=True
    for n in graph[node]:
        if visited[n]==False:
            cnt = dfs(n,cnt+1)

    return cnt        
n = int(input())
for _ in range(n):
    N,M = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):

        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = [False]*(N+1)
    cnt = dfs(1,0)
    print(cnt)


