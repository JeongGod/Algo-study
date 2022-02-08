from collections import defaultdict
from itertools import combinations
from operator import itemgetter
from typing import DefaultDict, List, Set, Tuple


def solution(orders: List[str], courses: List[int]):
    answer: List[str] = []

    for course in courses:
        max_order_cnt: int = 0
        possible_menus: Set[Tuple[str]] = set()
        course_meal: DefaultDict[str, int] = defaultdict(int)

        # 손님들이 주문한 메뉴로부터 현재 코스에서 가능한 코스요리 메뉴 조합을 모두 구한다.
        for order in orders:
            if len(order) >= course:
                possible_menus = possible_menus | set(
                    map(tuple, list(map(lambda x: sorted(x), combinations(order, course)))))

        # 가능한 코스요리 메뉴가 손님들이 주문한 메뉴에 있으면 해당 코스요리 주문 횟수를 추가
        for menus in possible_menus:
            for order in orders:
                if len(order) < course:
                    continue

                if len(set(menus) & set(order)) == course:
                    course_meal["".join(menus)] += 1

        # 코스요리 메뉴별 주문한 횟수를 기준으로 내림차순 정렬
        course_meal_list: List[Tuple[str, int]] = sorted(course_meal.items(),
                                                         key=itemgetter(1), reverse=True)

        if course_meal_list:
            max_order_cnt = course_meal_list[0][1]
            for info in course_meal_list:
                menu, order_cnt = info
                if order_cnt == max_order_cnt and order_cnt >= 2:
                    answer.append(menu)

    return sorted(answer)


# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
# print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
