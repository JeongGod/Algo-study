def solution(stones, k):
    left, right = 1, 200000000

    while left <= right:
        mid = (left+right)//2
        cnt = 0
        for num in stones:
            if num <= mid:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1
    return left
