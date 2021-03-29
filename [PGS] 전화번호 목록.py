from collections import Counter
def solution(phone_book):

    pbook = Counter(phone_book)

    for i in phone_book:
        for j in range(1,len(i)):
            if pbook[i[:j]]:
                return False

    return True