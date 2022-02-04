from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []
    for idx in course:
        candi = defaultdict(int)
        for order in orders:
            order = list(''.join(order))
            order.sort()
            for ret in list(map(''.join,combinations(order,idx))):
                candi[ret] += 1
                
        candi = sorted(candi.items(), key = lambda x : x[1], reverse = True)
        if(len(candi) > 0):
            mx = candi[0][1]
            if(mx  == 1):
                continue
            for el in candi:
                if(el[1] == mx ):
                    answer.append(el[0])
    answer.sort()
    return answer