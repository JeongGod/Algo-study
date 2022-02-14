import bisect


def solution(info, query):
    answer = []

    lang = ['cpp', 'java', 'python', '-']
    pos = ['backend', 'frontend', '-']
    career = ['junior', 'senior', '-']
    food = ['chicken', 'pizza', '-']

    tables = {}
    for a in lang:
        for b in pos:
            for c in career:
                for d in food:
                    tmp = a + b + c + d
                    tables[tmp] = []

    for candidate in info:
        string = candidate.split(' ')
        lang = [string[0], '-']
        pos = [string[1], '-']
        career = [string[2], '-']
        food = [string[3], '-']

        for a in lang:
            for b in pos:
                for c in career:
                    for d in food:
                        key = a + b + c + d
                        tables[key].append(int(string[4]))

    for key, value in tables.items():
        tables[key] = sorted(value)

    for candidate in query:
        candi, score = candidate.replace(' and ', '').split(' ')
        score = int(score)
        size = len(tables[candi])
        num = size - bisect.bisect_left(tables[candi], score, lo=0, hi=size)

        answer.append(num)

    return answer
