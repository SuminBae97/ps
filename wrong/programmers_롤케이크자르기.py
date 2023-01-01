from collections import Counter

def solution(topping):
    mine = Counter(topping)
    answer=  0
    other = {}
    for i in range(len(topping)):
        if topping[i] in other:
            other[topping[i]]+=1
        else:
            other[topping[i]]=1

        mine[topping[i]]-=1

        if mine[topping[i]]==0:
            del mine[topping[i]]


        if len(mine)==len(other):
            answer+=1
    return answer