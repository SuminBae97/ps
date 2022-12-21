import sys
input = sys.stdin.readline
 
import sys
n = int(input())

arr = [0]*(n+1)

for _ in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    arr[a]+=1
    arr[b]+=1


m = int(input())

for _ in range(m):
    t,k = map(int,sys.stdin.readline().split())
    if t==1:
        ans = arr[k]
        if ans!=1:
            print("yes")
        else:
            print("no")
    elif t==2:
        print("yes")