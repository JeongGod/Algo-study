from collections import Counter, defaultdict
from itertools import combinations


def solution(orders, course):
    """
    2명이상에게 주문된 세트메뉴
    """
    answer = []
    menus = defaultdict(list)
    # 모든 메뉴의 경우의 수를 구한다.
    for order in orders:
        for cnt in range(2, len(orders)+1):
            for menu in combinations(sorted(order), cnt):
                menus[cnt].append(menu)
    
    # 코스별로 가능한 메뉴를 본다.
    for cnt in course:
        if menus[cnt]:
            sorted_menu = Counter(menus[cnt]).most_common()
            top = sorted_menu[0][1]
            for key, val in sorted_menu:
                if top > val or val < 2:
                    break
                answer.append("".join(key))
    return sorted(answer)
