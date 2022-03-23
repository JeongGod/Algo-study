def solution(n, left, right):
    answer = []
    start_row, start_col = left // n, left % n
    end_row, end_col = right // n, right % n
    i = start_row
    j = start_col
    while True:
        idx = max(i, j) + 1
        answer.append(idx)
        if(i == end_row and j == end_col):
            break
        j += 1
        if(j == n):
            j = 0
            i += 1
    return answer