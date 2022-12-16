import sys

words = []
for i in range(5):
    a = list(input())
    l = 15 - len(a)
    tmp = ["" for _ in range(l)]
    a = a+tmp
    words.append(a)

total = ""
for i in range(15):
    tmp = ""
    for j in range(5):
        if words[j][i]=="":
            continue
        else:
            tmp+=words[j][i]
    total+=tmp

print(total)