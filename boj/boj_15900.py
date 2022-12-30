import sys
sys.setrecursionlimit(10**5)
n = int(input())
tree =[[] for _ in range(n+1)]
visited = [False]*(n+1)
distance = [0]*(n+1)

for _ in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(root):
    visited[root]=True
    for node in tree[root]:
        if visited[node]==False:
            distance[node] = distance[root]+1
            dfs(node)

leaf_node =[]

for i in range(2,len(tree)):
    if len(tree[i])==1:
        leaf_node.append(i)

dfs(1)

answer = 0
for val in leaf_node:
    answer+=distance[val]

if answer%2==0:
    print("No")
else:
    print("Yes")

