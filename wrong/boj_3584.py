import sys
t = int(input())

for _ in range(t):
    n = int(input())
    parent = [0]*(n+1) 
    for _ in range(n-1):
        a,b = map(int,sys.stdin.readline().split())
        parent[b]=a

    m,n = map(int,sys.stdin.readline().split())
    parent_m = [m]
    parent_n = [n]


    while parent[m]:
        parent_m.append(parent[m])
        m = parent[m]

    while parent[n]:
        parent_n.append(parent[n])
        n= parent[n]

    last_m = len(parent_m)-1
    last_n = len(parent_n)-1

    while parent_m[last_m]==parent_n[last_n]:
        last_m-=1
        last_n-=1

    print(parent_m[last_m+1])





