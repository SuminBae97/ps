import sys
sys.setrecursionlimit(10**6)
n = int(input())

tree = [[] for _ in range(n+1)]
parent = [0]*(n+1)
visited = [False]*(n+1)

for _ in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(x):
    visited[x]=True
    for node in tree[x]:
        if visited[node]==False:
            parent[node]= x
            dfs(node)

dfs(1)
for i in range(2,n+1):
    print(parent[i])
