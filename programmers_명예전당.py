def solution(k, score):
    i = 0
    fame = []
    answer=[]
    for val in score:
        if i < k:
            fame.append(val)
        elif i>=k:
            fame.append(val)
            fame.sort(reverse=True)
            fame = fame[:k]   
        i+=1
        fame.sort(reverse=True)
        answer.append(fame[-1])
    return answer