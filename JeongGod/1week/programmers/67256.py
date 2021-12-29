def solution(numbers, hand):
    """
    1. (3, 0), (3, 2)가 출발점
    2. (x, 0)왼쪽, (x, 2)오른쪽, (x, 1)은 현재 엄지손가락과 가까운 친구
    3. 만약 거리가 같다면 왼손잡이는 왼, 오른손잡이는 오른

    1차원배열로 진행, 3으로 나눠서 가자
    """
    keypad = [0] * 11
    answer = ""
    cur = [9, 11]
    for num in map(lambda x: x - 1, numbers):
        if num == -1:
            num = 10
        div, mod = divmod(num, 3)
        if mod == 0:
            cur[0] = num
            answer += "L"
        elif mod == 2:
            cur[1] = num
            answer += "R"
        # 가운데 부분
        else:
            min_dist = 5
            dists = []
            for i in cur:
                a, b = divmod(i, 3)
                dist = abs(a - div) + abs(b - mod)
                dists.append(dist)

            if dists[0] < dists[1]:
                answer += "L"
                cur[0] = num
            elif dists[0] > dists[1]:
                answer += "R"
                cur[1] = num
            else:
                if hand == "left":
                    answer += "L"
                    cur[0] = num
                else:
                    answer += "R"
                    cur[1] = num

    return answer
