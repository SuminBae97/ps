def solution(common):
    
    f = common[0]
    s = common[1]
    t = common[2]

    if (s-f)==(t-s):
        return (common[-1]+(s-f))

    elif (s//f)==(t//s):
        return (common[-1]*(t//s))