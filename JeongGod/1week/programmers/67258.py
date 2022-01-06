from collections import defaultdict


def solution(gems):
    answer = []
    num = len(set(gems))
    """
    1. 처음 시작 gem을 기억한다.
    2. 만약 시작 gem과 같은 놈을 만난다면 시작 gem의 위치를 바꾼다.
        1. 먼저 지금까지 gem의 개수를 센 dict형식을 갖고 있는다.
        2. 바꾼 gem의 위치에 있는 개수를 -1 을한다.
        3. 만약 해당 gem의 개수가 1이 된다면 그만둔다.
        4. 그렇지 않다면 1이 될때까지 한 칸씩 앞으로 간다.
    3. 그렇게 진행하다가 모든 gem을 갖고 있는 길이가 된다면 answer에 넣는다. (길이, [x, y])
    4. answer를 길이가 가장 작은 친구를 뽑아 x, y를 리턴한다.
    """
    result = defaultdict(int)
    left, right = 0, 0

    while right < len(gems):
        # 지금까지 gem의 개수를 기억한다.
        result[gems[right]] += 1
        # 시작 gem과 같은 gem이 나온다면
        if result[gems[left]] == 2:
            # left를 늘려가며 1이 될때까지 반복한다.
            while left < right:
                result[gems[left]] -= 1
                left += 1
                if result[gems[left]] == 1:
                    break

        # 지금 갖고 있는 gem이 모든 gem을 갖고 있다면
        if len(result) == num:
            answer.append((right - left, [left + 1, right + 1]))
        right += 1

    return min(answer, key=lambda x: x[0])[1]
