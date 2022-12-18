import sys
n,q = map(int,input().split())
num = []
vis = set()
for _ in range(q):
    a = int(sys.stdin.readline().rstrip())
    num.append(a)

def dfs(x):
    ans = 0
    duck = x
    while duck>0:
        if duck in vis:
            ans = duck
        duck = duck//2

    if ans==0:
        vis.add(x)
    print(ans)


for i in num:
    dfs(i)