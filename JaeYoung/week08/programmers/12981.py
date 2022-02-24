import math


def solution(n, words):
    answer = [0, 0]
    record = []

    for idx, word in enumerate(words):
        if record and record[-1][-1] != word[0] or word in record:
            person = n if (idx + 1) % n == 0 else (idx + 1) % n
            turn = math.ceil((idx + 1) / n)
            answer[0] = person
            answer[1] = turn
            break

        if not word in record:
            record.append(word)

    return answer
