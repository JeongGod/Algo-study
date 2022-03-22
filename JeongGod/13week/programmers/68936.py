answer = [0, 0]

def check_compress(arr, sx, sy, ex, ey):
    val = arr[sx][sy]
    for x in range(sx, ex+1):
        for y in range(sy, ey+1):
            if arr[x][y] != val:
                return False
    return True

def dfs(arr, sx, sy, ex, ey):
    # 종료 조건
    if ex - sx <= 0 or check_compress(arr, sx, sy, ex, ey):
        answer[arr[sx][sy]] += 1
        return
    # 전체 탐색
    half_x, half_y = (sx + ex) // 2, (sy + ey) // 2
    dfs(arr, sx, sy, half_x, half_y)
    dfs(arr, half_x+1, sy, ex, half_y)
    dfs(arr, sx, half_y+1, half_x, ey)
    dfs(arr, half_x+1, half_y+1, ex, ey)
    
def solution(arr):
    """
    쿼드 트리 => 자식이 4개있는 트리.
    """
    n = len(arr)
    dfs(arr, 0, 0, n-1, n-1)
    return answer
