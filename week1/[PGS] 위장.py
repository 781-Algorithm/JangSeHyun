from collections import defaultdict as ddict

def solution(clothes):

    answer = 1
    look = ddict(list)

    for cloth in clothes:
        look[cloth[1]].append(cloth[0])
    
    for category in look.keys():
        answer *= (1+len(look[category]))
    
    return answer-1