def solution(survey, choices):
    answer = ''
    t =[
    ['R','T'],
    ['C','F'],
    ['J','M'],
    ['A','N']
    ]

    scores = {
        'R':0,
        'T':0,
        'C':0,
        'F':0,
        'J':0,
        'M':0,
        'A':0,
        'N':0
    }
    
    for val,cho in zip(survey,choices):
        first  =val[0]
        second = val[1]
        if cho>4:
            scores[second]+=(cho-4)
        else:
            scores[first] +=(4-cho)


    for v in t:
        if scores[v[0]] >= scores[v[1]]:
            answer+=v[0]
        else:
            answer+=v[1]
    return answer