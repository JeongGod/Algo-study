from typing import List


def sum_times(food_times: List[int], pivot: int) -> int:
    return sum(time if time < pivot else pivot for time in food_times)


def count_iteration(food_times: List[int], k: int) -> int:
    start: int = 0
    end: int = 10 ** 9

    while start <= end:
        mid: int = (start + end) // 2

        if sum_times(food_times, mid) <= k:
            start = mid + 1
        else:
            end = mid - 1

    return end


def solution(food_times: List[int], k: int) -> int:
    iters: int = count_iteration(food_times, k)
    time: int = k - sum_times(food_times, iters)
    foods: List[int] = [food for food, time in enumerate(food_times) if time > iters]
    return foods[time] + 1 if foods else -1


# 1
print(solution([3, 1, 2], 5))
# 1
print(solution([2, 2, 2], 3))
# 2
print(solution([2, 2, 2], 4))
# -1
print(solution([1, 1, 1, 1], 4))
