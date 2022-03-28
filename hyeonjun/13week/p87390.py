def solution(n, left, right):
    arr = []
    left, right = int(left), int(right)
    for i in range(left//n+1, right//n+2):
        for j in range(i, n+1):
            if j == i:
                arr += [j for _ in range(j)]
            else:
                arr += [j]

    return arr[left % n:] if not (right+1) % n else arr[left % n:len(arr)-(n-(right+1) % n)]
