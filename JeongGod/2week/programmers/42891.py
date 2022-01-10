def solution(food_times, k):
    """
    1. food_times를 (time, index)로 time순으로 정렬한다.
    2. 하나씩 pop하면서 time * len(food_times)만큼 시간이 흐른다고 생각한다.
    3. 만약 그 전에, k를 만나게 된다면 현재 k % len(food_times) => k초가 흐른 뒤에 먹는 index의 값
    4. 그 값을 리턴한다.
    """
    sort_food_times = sorted(enumerate(food_times), key=lambda x: (x[1], x[0]), reverse=True)
    answer = 0
    spend_time = 0
    before_time = 0
    while sort_food_times:
        # 가장 시간이 적은 음식
        idx, time = sort_food_times[-1]
        # 해당 음식을 먹는데 얼마나 썼는지
        spend_time = ((time - before_time) * len(sort_food_times))
        # 만약 해당 음식을 먹다가 네트워크 중단이 일어났다면
        if k < spend_time:
            idx_sort_food_times = sorted(sort_food_times, key=lambda x: x[0])
            return idx_sort_food_times[k % len(sort_food_times)][0] + 1
        k -= spend_time
        before_time = time
        while sort_food_times:
            if time != sort_food_times[-1][1]:
                break
            sort_food_times.pop()
    return -1