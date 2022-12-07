import sys
sys.setrecursionlimit(10**6)
n = int(input())

tree = [[] for _ in range(n+1)]
parent = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(start):
    visited[start]=True
    for n in tree[start]:
        if visited[n]==False:
            parent[n] =  start
            dfs(n)

dfs(1)
            
for i in range(2,n+1):
    print(parent[i])

    

