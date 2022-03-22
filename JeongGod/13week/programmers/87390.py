answer = []
def insert_ans(x, sy, ey):
    global answer
    val = x+1
    if sy > x:
        val += (sy-x-1)

    for y in range(sy, ey):
        if y <= x:
            answer.append(val)
        else:
            val += 1
            answer.append(val)
    
def solution(n, left, right):
    
    lrow, lcol = map(int, [left // n, left % n])
    rrow, rcol = map(int, [right // n, right % n])

    for x in range(lrow, rrow+1):
        # 처음과 마지막은 따로 처리
        if x == lrow and x == rrow:
            insert_ans(x, lcol, rcol+1)
            break
        if x == lrow:
            insert_ans(x, lcol, n)
        elif x == rrow:
            insert_ans(x, 0, rcol+1)
        else:
            insert_ans(x, 0, n)
            
    return answer
