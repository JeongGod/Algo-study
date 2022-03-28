def solution(n, left, right):
    answer = []
    for i in range(int(left), int(right) + 1):
        x = i // n
        y = i % n
        if x >= y:
            answer.append(x + 1)
        else:
            answer.append(y + 1)
    return answer