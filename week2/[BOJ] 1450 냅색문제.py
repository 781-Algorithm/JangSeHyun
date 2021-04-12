# 1450 - 냅색문제 (meet in the middle 알고리즘)==> 시간 초과난 풀이! 아마 itertools를 
# 써서도 그렇고, 맨밑에 for문 두개도는 부분에서 걸린거 같다.
from itertools import combinations
n,c = map(int,input().split())
weight = list(map(int,input().split()))

if n!=1:
    
    middle = n//2
    A, B = weight[:middle], weight[middle:]
    # 앞에껀 middle개(index 0 ~ middle-1) 뒤에껀 n-middle개

    # n이 1일때 처리 해줘야 함?
    sum_A, sum_B = [], []
    result = 1

    for i in range(1,middle+1):
        temp_comb = combinations(A,i)
        for j in temp_comb:
            temp_sum = sum(j)
            if temp_sum > c:
                continue
            sum_A.append(temp_sum)
            result += 1

    for i2 in range(1,n-middle+1):
        temp_comb = combinations(B,i2)
        for j2 in temp_comb:
            temp_sum = sum(j2)
            if temp_sum > c:
                continue
            sum_B.append(temp_sum)
            result += 1

    sum_A.sort()
    sum_B.sort(reverse=True)

    for i in range(len(sum_A)):
        for j in range(len(sum_B)):
            if sum_A[i] + sum_B[j] <= c:
                result += (len(sum_B)-j)
                break
    print(result)

else:
    print(1 if weight[0]>c else 2)

# 다른 풀이 --> 아까꺼 for문을 bisect로 바꿔줬더니 통과했다. (조금 가뿐히..) 
# combination은 큰 문제가 없던걸까. 혹시 모르니까 쟤를 브루트포스로 구현하는 것도 알아야 함.
from itertools import combinations
from bisect import bisect_right
n,c = map(int,input().split())
weight = list(map(int,input().split()))

if n!=1:

    middle = n//2
    A, B = weight[:middle], weight[middle:]
 
    sum_A, sum_B = [], []
    result = 1

    for i in range(1,middle+1):
        temp_comb = combinations(A,i)
        for j in temp_comb:
            temp_sum = sum(j)
            if temp_sum > c:
                continue
            sum_A.append(temp_sum)
            result += 1

    for i2 in range(1,n-middle+1):
        temp_comb = combinations(B,i2)
        for j2 in temp_comb:
            temp_sum = sum(j2)
            if temp_sum > c:
                continue
            sum_B.append(temp_sum)
            result += 1

    sum_B.sort()

    for i in range(len(sum_A)):
        result += bisect_right(sum_B,c-sum_A[i])
    print(result)

else:
    print(1 if weight[0]>c else 2)

# 브루트 포스로 직접 구현 --> 앞에보다 살짝 빠르다 (120ms --> 108ms)
from bisect import bisect_right
n,c = map(int,input().split())
weight = list(map(int,input().split()))

if n!=1:

    middle = n//2
    A, B = weight[:middle], weight[middle:]

    sum_A, sum_B = [0], [0]

    for i in range(middle):
        temp = []
        for x in sum_A:
            temp.append(weight[i]+x)
        sum_A += temp

    for i in range(middle,n):
        temp = []
        for x in sum_B:
            temp.append(weight[i]+x)
        sum_B += temp

    result = 0
    sum_B.sort()

    for i in range(len(sum_A)):
        result += bisect_right(sum_B,c-sum_A[i])
    print(result)

else:
    print(1 if weight[0]>c else 2)