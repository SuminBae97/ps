from collections import Counter
str = input()
str = str.split(" ")
ct = Counter(str)

sum = 0

for val in ct:
    if val =='':
        pass
    else:
        sum+=ct[val]

print(sum)