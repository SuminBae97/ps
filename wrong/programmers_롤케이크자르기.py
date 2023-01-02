from collections import Counter

def solution(topping):
    ct = Counter(topping)
    others ={}
    answer = 0
    for i in range(len(topping)):
        if topping[i] in others:
            others[topping[i]]+=1
        else:
            others[topping[i]] = 1

        ct[topping[i]]-=1

        if ct[topping[i]]==0:
            del ct[topping[i]]

        if len(others)== len(ct):
            answer+=1
    return answer