import sys
sys.setrecursionlimit(10**5)
n = int(input())

visited = [False]*(n+1)
tree = [[] for _ in range(n+1)]
parent = [0]*(n+1)

for _ in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(root):
    visited[root]=True
    for val in tree[root]:
        if visited[val]==False:
            parent[val]=root
            dfs(val)

dfs(1)
for i in range(2,len(parent)):
    print(parent[i])
