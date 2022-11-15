def solution(lines):
    line = []
    for vals in lines:
        line.append(vals[0])
        line.append(vals[1])
    max_num = max(line)
    min_num = min(line)

    data = []

    for i in range(min_num , max_num):
        data.append([[i,i+1],0])

    for val in lines:
        for i in range(val[0],val[1]):
            tmp = [i,i+1]
            for d in data:
                tmp2 = d[0]
                if tmp2==tmp:
                    d[1]+=1

    count = 0

    for val in data:
        if val[1]>1:
            count+=1
    return count

