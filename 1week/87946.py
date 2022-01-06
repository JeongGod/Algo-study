from itertools import permutations

def solution(k, dungeons):
    answer = -1
    for case in permutations(dungeons):
        health = k
        cnt = 0
        for el in case:
            if(el[0] <= health):
                cnt += 1
                health -= el[1]
            else:
                break
        answer = max(answer, cnt)
    return answer