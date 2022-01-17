def calc(pri, a):
    for target in a[1:-1]:
        if target < pri:
            pri = target
            arr.add(target)
    return 0


def solution(a):
    global arr
    length = len(a)

    if length < 3:
        answer = length
        return answer

    answer = 2
    arr = set()

    calc(a[0], a)
    calc(a[-1], list(reversed(a)))

    return answer + len(arr)
