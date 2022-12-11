def solution(s):
    s = list(s)
    anchor = ""
    anchor_count = 1
    other_count = 0

    index = 1
    answer = 0



    while len(s)>0:
        if len(s) == index:    
            answer+=1    
            break    

        anchor = s[0]
        if anchor == s[index]:
            anchor_count+=1
            index+=1
        else:
            other_count+=1
            if other_count == anchor_count:
                del s[:index+1]
                answer+=1
                anchor_count = 1
                other_count = 0
                index=1

            else:
                index+=1
    return answer