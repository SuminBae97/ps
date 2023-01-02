import sys
n,m = map(int,sys.stdin.readline().split())
d = set()
b = set()

for _ in range(n):
    d.add(input())
for _ in range(m):
    b.add(input())

answer = d&b
answer = list(answer)
answer.sort()
print(len(answer))
for val in answer:
    print(val)