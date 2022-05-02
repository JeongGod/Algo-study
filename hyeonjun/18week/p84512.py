replace = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}


def solution(word):
    answer, length, tmp = 0, len(word)-1, 0
    for idx in range(4, -1, -1):
        if idx > length:
            tmp *= 5
            tmp += 5
            continue
        if idx != length:
            tmp = 0
            for _ in range(4-idx):
                tmp *= 5
                tmp += 5
        answer += replace[word[idx]]*(tmp+1) + 1
    return answer
