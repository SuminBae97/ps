import sys
# 5
# 2 3
# 3 4
# 3 1
# 1 5
# 3 5
n = int(input())
parent = [0]*(n+1)
for _ in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    parent[b] =a
print(parent)
a,b = map(int,sys.stdin.readline().split())
parent_a = [a]
parent_b = [b]

while parent[a]:
    parent_a.append(parent[a])
    a = parent[a]

while parent[b]:
    parent_b.append(parent[b])
    b = parent[b]

print(parent_b)
a_root = len(parent_a)-1
b_root = len(parent_b)-1

while parent_a[a_root]==parent_b[b_root]:
    a_root-=1
    b_root-=1
print(parent_a[a_root+1])