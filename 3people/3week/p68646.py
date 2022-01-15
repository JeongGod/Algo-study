def solution(a):
    answer = 2
    if 0 <= len(a) <= 2:
        return len(a)
    front, rear = a[0], a[-1]
    for i in range(1, len(a) - 1):
        if front > a[i]:
            answer += 1
            front = a[i]
        if rear > a[-1-i]:
            answer += 1
            rear = a[-1-i]
    return answer - 1 if front == rear else answer