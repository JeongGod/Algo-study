import re
from itertools import permutations
from heapq import heappush


def solution(user_id, banned_id):
    answer = set()
    regexes = []
    for ban_regex in banned_id:
        regex = ''
        for letter in ban_regex:
            if letter == '*':
                regex += '\w'
            else:
                regex += letter
        regex += '$'
        regexes.append(regex)

    cases = permutations([i for i in range(len(user_id))], len(banned_id))
    for case in cases:
        flag = True
        tmp = []
        for idx, regex in enumerate(regexes):
            if not re.match(regex, user_id[case[idx]]):
                flag = False
                break
            else:
                tmp.append(case[idx])
        if flag:
            tmp.sort()
            answer.add(tuple(tmp))

    return len(answer)
