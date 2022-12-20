import sys
alpha = {
    'A':3,
    'B':2,
    'C':1,
    'D':2,
    'E':3,
    'F':3,
    'G':3,
    'H':3,
    'I':1,
    'J':1,
    'K':3,
    'L':1,
    'M':3,
    'N':3,
    'O':1,
    'P':2,
    'Q':2,
    'R':2,
    'S':1,
    'T':2,
    'U':1,
    'V':1,
    'W':2,
    'X':2,
    'Y':2,
    'Z':1
}

code = input()
a = []
for val in code:
    a.append(alpha[val])

while len(a)!=1:
    tmp = []
    for i in range(0,len(a),2):
        if i==len(a)-1:
            if a[i]>=10:
                t = a[i]%10
                tmp.append(t)
            else:
                tmp.append(a[i])
            
        else:
            t = a[i]+a[i+1]
            if t>10:
                tmp.append(t%10)
            else:
                tmp.append(t)

    a = tmp
val = 0
if a[0]>10:
    val = a[0]%10
else:
    val = a[0]

if val==0 or val%2==0:
    print("You're the winner?")
else:
    print("I'm a winner!")


