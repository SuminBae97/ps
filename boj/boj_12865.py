import sys
bags =[[0,0]]
n,k = map(int,sys.stdin.readline().split())
dp = [[0]*(k+1) for _ in range(n+1)]

for _ in range(n):
    w,v = map(int,sys.stdin.readline().split())
    bags.append([w,v])

for i in range(1,n+1):
    for j in range(1,k+1):
        w = bags[i][0]
        v = bags[i][1]

        if j<w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
print(dp[n][k])
