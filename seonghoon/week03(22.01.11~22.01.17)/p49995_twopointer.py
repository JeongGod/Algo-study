from typing import List


def split(m: int, cookies: List[int], length: int) -> int:
    left: int = m
    right: int = m + 1
    sum_left: int = cookies[left]
    sum_right: int = cookies[right]
    max_cookie: int = 0

    while 0 <= left or right < length:
        if sum_left == sum_right:
            max_cookie = sum_right

        if sum_left <= sum_right and 0 <= left - 1:
            left -= 1
            sum_left += cookies[left]
        elif sum_left > sum_right and right + 1 < length:
            right += 1
            sum_right += cookies[right]
        else:
            break

    return max_cookie


def solution(cookies: List[int]) -> int:
    answer: int = 0
    length: int = len(cookies)

    for m in range(length - 1):
        answer = max(answer, split(m, cookies, length))

    return answer


# 3
print(solution([1, 1, 2, 3]))
# 0
print(solution([1, 2, 4, 5]))
