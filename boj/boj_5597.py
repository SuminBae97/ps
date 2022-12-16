import sys
people =[i for i in range(1,31)]

for i in range(28):
    n = int(input())
    people.remove(n)
for val in people:
    print(val)