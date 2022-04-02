import math


def dfs(start, end, a, b, cnt):
    global answer
    if not (start <= a <= end and start <= b <= end):
        answer = max(answer, cnt-1)
        return
    mid = (start + end) // 2
    dfs(start, mid, a, b, cnt+1)
    dfs(mid+1, end, a, b, cnt+1)
def solution(n,a,b):
    global answer
    answer = 0
    """
    2^n이면 2^n-1씩 쪼개진다.
    그러면 2^n-1 범위안에 존재하는지 판단하고 해당 친구를 쪼개면서 진행하자.
    """
    dfs(0, n, a, b, 0)

    return int(math.log2(n) - answer)
