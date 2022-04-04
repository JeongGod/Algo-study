def solution(A, B):
    answer = 0
    length = len(A)
    A.sort()
    B.sort()
    index_A = 0
    index_B = 0
    while index_A < length and index_B < length:
        if A[index_A] < B[index_B]:
            index_A += 1
            answer += 1
        index_B += 1
    return answer
