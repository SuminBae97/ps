n, q = map(int, input().split())
ducks = [int(input())for _ in range(q)]
visited = set()

def dfs(val):
    ans = 0 
    duck = val
    while duck > 0:
        if duck in visited:
            ans = duck
        duck = duck//2
    
    if ans == 0:
        visited.add(val)
    print(ans)

for i in ducks:
    dfs(i)