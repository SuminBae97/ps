def solution(s):
    answer = []
    n = len(s)
    tmp = [-1]
    flag = False
    for i in range(1,n):
        val = -1
        v = s[i]
        cnt = 0
        for j in range(i-1,-1,-1):
            cnt+=1
            if s[j]==s[i]:
                tmp.append(cnt)
                flag=True
                break
        if flag!=True:
            tmp.append(-1)
        else:
            flag=False   

    return tmp