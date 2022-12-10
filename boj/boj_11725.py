import sys
sys.setrecursionlimit(10**6)
n = int(input())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
parent = [0 for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)




def dfs(start):
    visited[start]=True
    for node in graph[start]:
        if visited[node]==False:
            parent[node]=start
            dfs(node)
dfs(1)
for i in range(2,n+1):
    print(parent[i])
    


