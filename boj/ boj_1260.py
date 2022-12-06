import sys
sys.setrecursionlimit(10**6)
from collections import deque

n,m,v  = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)
for node in graph:
    node.sort()

def dfs(start):
    visited[start]=True
    print(start,end=' ')
    for node in graph[start]:
        if visited[node]==False:
            dfs(node)

def bfs(start):
    visited[start]=False
    q = deque([start])

    while q:
        
        node = q.popleft()
        print(node,end=" ")
        for v in graph[node]:
            if visited[v]==True:
                q.append(v)
                visited[v]=False

dfs(v)
print()
bfs(v)






