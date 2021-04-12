def solution(prices):

    length = len(prices)
    answer = [0]*length
    stack = []

    for i,value in enumerate(prices):
        
        while stack and value < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i-j
        stack.append(i)
    
    while stack:
        q = stack.pop()
        answer[q] = length-1-q
            
    return answer