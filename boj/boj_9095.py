
t = int(input())
dp = [0]*(12)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(t):
    n = int(input())
    for j in range(4,n+1):
        dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
    print(dp[n])    
    
