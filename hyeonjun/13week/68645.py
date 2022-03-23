def solution(n):
    answer = []
    down_right = [[] for _ in range(n)]  # 아래진행 + 우측진행만 저장하는 배열
    up = [[] for _ in range(n)]  # 위로진행만 저장하는 배열

    ceiling = 0
    floor = n-1
    num = 1

    while n:
        for i in range(n):
            down_right[ceiling+i].append(num)
            num += 1
        ceiling += 2
        n -= 1
        if not n:
            break

        for i in range(n):
            down_right[floor].append(num)
            num += 1
        floor -= 1
        n -= 1
        if not n:
            break

        for i in range(n):
            up[floor-i].append(num)
            num += 1
        n -= 1

    for i in range(len(up)):
        answer += (down_right[i] + up[i][::-1])

    return answer
