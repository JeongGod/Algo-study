def check(val, stones, k):
    cnt = 0
    for s in stones:
        if s <= val:
            cnt += 1
        else:
            cnt = 0
        if cnt == k:
            return False
    return True
def solution(stones, k):
    left, right = 0, 200_000_000
    while left <= right:
        mid = (left + right) // 2
        # 가능하다면
        if check(mid, stones, k):
            left = mid + 1
        else:
            right = mid - 1
    return left
