from itertools import permutations

def solution(babbling):
    answer = 0
    baby_words = ['aya','ye','woo','ma']
    total_words=[]
    for i in range(1,len(baby_words)+1):
        
        for j in permutations(baby_words,i):
            total_words.append(''.join(j))
    
    for word in babbling:
        if word in total_words:
            answer+=1
            
    
    return answer

print(solution(['aya','ye','wwo']))    