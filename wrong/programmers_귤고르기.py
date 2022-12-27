from collections import Counter
from itertools import permutations,combinations

def solution(k, tangerine):
    
    count = sorted(Counter(tangerine).items(),reverse = True, key = lambda x : x[1])

    answer=0

    for key,value in count:
        if k<=0:
            break
        k = k-value
        answer+=1
    return answer
