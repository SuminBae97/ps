class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        
        bags = [[0,0]]
        for w,v in zip(wt,val):
            bags.append([w,v])
            
        dp = [[0]*(W+1) for _ in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,W+1):
                w = bags[i][0]
                v = bags[i][1]
                
                if j<w:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j-w]+v, dp[i-1][j])
        return dp[n][W]
       