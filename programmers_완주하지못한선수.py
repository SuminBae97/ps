from collections import Counter
def solution(participant, completion):
    cp = Counter(participant)
    cc = Counter(completion)

    answer = cp-cc
    for val in answer:
        return val