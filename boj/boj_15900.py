import sys
sys.setrecursionlimit(10**5)
n = int(input())
tree = [[] for _ in range(n+1)]
visited = [False]*(n+1)

dist = [0]*(n+1)

for _ in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(root):
    visited[root]=True
    for val in tree[root]:
        if visited[val]==False:
            dist[val]= dist[root] + 1
            dfs(val)
dfs(1)
answer = 0
for i in range(2,len(tree)):
    if len(tree[i])==1:
        answer+=dist[i]

if answer%2==0:
    print("No")
else:
    print("Yes")

