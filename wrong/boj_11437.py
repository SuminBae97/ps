import sys
sys.setrecursionlimit(10**6)

n = int(input())
tree =[[] for _ in range(n+1)]
parent = [0]*(n+1)
visited = [False]*(n+1)
level = [0]*(n+1)

for _ in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(x,dst):
	visited[x]=True
	level[x] = dst
	
	for node in tree[x]:
		if visited[node]==False:
			parent[node]=x
			dfs(node,dst+1)

dfs(1,0)

def lcs(a,b):
    while level[a]!=level[b]:
		if level[a]>level[b]:
			a = parent[a]
		else:
			b = parent[b]

	while a!=b:
		a = parent[a]
		b = parent[b]       