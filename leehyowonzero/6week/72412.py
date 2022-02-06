from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(information, queries):
    answer = []
    conditiondict = defaultdict(list)
    for info in information:
        info = info.split()
        condition = info[:-1]  
        score = int(info[-1])
        for i in range(5):
             for c in combinations(condition, i):
                tmp = ''.join(c)
                conditiondict[tmp].append(score) 

    for value in conditiondict.values():
        value.sort()   

    for query in queries:
        query = query.replace("and ", "")
        query = query.replace("- ", "")
        query = query.split()
        target_key = ''.join(query[:-1])
        target_score = int(query[-1])
        count = 0
        if target_key in conditiondict:
            target_list = conditiondict[target_key]
            idx = bisect_left(target_list, target_score)
            count = len(target_list) - idx
        answer.append(count)      
    return answer