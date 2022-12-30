from collections import Counter
def solution(want, number, discount):
    tmp =[]
    for w,n in zip(want,number):
        tmp1 =[w]*n
        tmp+=tmp1

    ct = Counter(tmp)
    answer = 0
    for i in range(len(discount)):
        ds = discount[i:i+10]
        dst = Counter(ds)
        if len(ct-dst)==0:
            answer+=1
    return answer

