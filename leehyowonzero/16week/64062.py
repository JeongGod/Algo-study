def solution(stones, k):
    answer = 200000000
    n = len(stones)
    arr = [[0 for _ in range(n)] for _ in range(k)]
    for i in range(n):
        arr[0][i] = stones[i]
    for i in range(1,k):
        for j in range(0,n-i):
            arr[i][j] = max(arr[i-1][j],arr[0][j+i])
    for i in arr[k-1]:
        if(i != 0 and i <answer ):
            answer = i
    return answer