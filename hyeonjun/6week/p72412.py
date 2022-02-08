import re


def solution(info, queries):
    answer = []

    for query in queries:
        regex = '.*'
        query = re.split(' and | ', query)
        for elm in query[:-1]:
            if elm != '-':
                regex += elm + ' .*'

        cnt = 0
        for person in info:
            if re.match(regex, person) and person[-3:] >= query[-1]:
                cnt += 1
        answer.append(cnt)

    return answer
