import sys
n = int(input())
house =[]

for _ in range(n):
    r,g,b = map(int,sys.stdin.readline().split())
    house.append([r,g,b])


for i in range(1,n):
    for j in range(len(house[i])):
        if j==0:
            house[i][j] = min(house[i-1][j+1],house[i-1][j+2])+house[i][j]
        elif j==1:
            house[i][j] = min(house[i-1][j-1], house[i-1][j+1]) + house[i][j]
        else:
            house[i][j] = min(house[i-1][j-1], house[i-1][j-2]) + house[i][j]  

print(min(house[-1]))  