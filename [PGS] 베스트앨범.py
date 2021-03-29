from collections import defaultdict as ddict
def solution(genres, plays):
    answer = []
    music = ddict(list)

    for i in range(len(genres)):
        music[genres[i]].append([plays[i],-i])
    
    total = []
    for i in music.keys():
        temp_sum = 0
        for j in music[i]:
            temp_sum += j[0]
        total.append([i,temp_sum])
    total.sort(key=lambda x:x[1],reverse=True)

    for g,_ in total:
        music[g].sort(reverse=True)

        if len(music[g])==1:
            answer.append(-music[g][0][-1])
        else:
            for i in range(2):    
                answer.append(-music[g][i][-1])

    return answer
