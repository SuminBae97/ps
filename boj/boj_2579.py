n = int(input())
s = [0 for i in range(301)]
dp  = [0 for i in range(301)]

for i in range(n):
    tmp = int(input())
    s[i] = tmp

dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1]+s[2] , s[2] + s[0])

for i in range(3,n):
    dp[i] = max(dp[i-2]+s[i] , dp[i-3]+s[i-1]+s[i])
print(dp[n-1])
