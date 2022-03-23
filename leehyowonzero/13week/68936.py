def check_full(target, x, y, n, arr):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if(target != arr[i][j]):
                return False
    return True

def check_square(x, y, n, arr):
    if(check_full(arr[x][y], x, y, n, arr)):
        answer[arr[x][y]] += 1
        return
    check_square(x, y, n//2, arr)
    check_square(x+n//2, y, n//2, arr)
    check_square(x, y+n//2, n//2, arr)
    check_square(x+n//2, y+n//2, n//2, arr)

def solution(arr):
    global answer 
    answer = [0, 0]
    check_square(0, 0 , len(arr), arr) # 시작 x좌표, y좌표, 검사하고자하는 사각형의 변의 길이, 배열
    return answer