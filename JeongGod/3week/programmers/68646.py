def solution(a):
    """
    1. 하나를 기준으로 왼쪽, 오른쪽중 가장 작은 놈을 찾는다.
    2. 왼쪽 작은 놈, 오른쪽 작은 놈 둘 다 작으면 불가능이다.
    """
    answer = 0
    left_min = []
    right_min = []
    left_min_val = a[0]
    right_min_val = a[-1]
    for val in a:
        if left_min_val > val:
            left_min_val = val
        left_min.append(left_min_val)

    for val in a[::-1]:
        if right_min_val > val:
            right_min_val = val
        right_min.append(right_min_val)
    right_min = right_min[::-1]

    for idx in range(len(a)):
        if idx == 0 or idx == len(a) - 1:
            answer += 1
            continue
        if a[idx] > right_min[idx+1] and a[idx] > left_min[idx-1]:
            continue
        answer += 1
    return answer