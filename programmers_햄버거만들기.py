def solution(ingredient):
    stack = []
    count = 0
    for val in ingredient:
        if len(stack)>=4:
            if stack[-1] == 1 and stack[-2] == 3 and stack[-3]==2 and stack[-4]==1:
                stack.pop(-1)
                stack.pop(-1)
                stack.pop(-1)
                stack.pop(-1)
                stack.append(val)
                count+=1

            else:
                stack.append(val)
        else:
            stack.append(val)

    if len(stack)>=4:
        if stack[-1] == 1 and stack[-2] == 3 and stack[-3]==2 and stack[-4]==1:
            stack.pop(-1)
            stack.pop(-1)
            stack.pop(-1)
            stack.pop(-1)
            count+=1

    return count

