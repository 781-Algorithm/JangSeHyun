# 프로그래머스 - (해시) 완주하지 못한 선수 --> defaultdict 괜찮은데?
from collections import defaultdict

def solution(participant, completion):
    marathon = defaultdict(int)

    for i in participant:
        if marathon[i]:
            marathon[i] += 1
        else:
            marathon[i] = 1

    for i in completion:
        marathon[i] -= 1

    for k, v in marathon.items():
        if v:
            return k

# 다른풀이.. 근데 이게 문제 목적에 부합한지 모르겠다. 파이써닉함

import collections
def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# 이게 뭔가 목적에 부합한듯 번뜩임 조금 필요
def solution3(participant, completion):

    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer