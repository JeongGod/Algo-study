def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    al, bl = 0, 0
    limit = len(A)
    while al < limit and bl < limit:
        if A[al] >= B[bl]:
            bl += 1
        else:
            answer += 1
            al += 1
            bl += 1
    return answer
