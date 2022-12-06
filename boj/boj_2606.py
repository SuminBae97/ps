import sys
sys.setrecursionlimit(10**6)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)

def dfs(start,cnt):
    visited[start]=True
    for node in graph[start]:
        if visited[node]==False:
            cnt = dfs(node,cnt+1)
    return cnt


print(dfs(1,0))  
