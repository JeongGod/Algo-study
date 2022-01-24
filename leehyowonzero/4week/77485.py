def show(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end = ' ')
        print()
    print()
    
def rotate(x1, y1, x2, y2): # 4방향 스왑형식으로 rotate 구현
    mn = float('inf')
    mn = min(mn, arr[x1][y1])
    for x in range(x1, x2):
        arr[x][y1], arr[x+1][y1] = arr[x+1][y1], arr[x][y1]
        mn = min(mn, arr[x][y1])
    for y in range(y1, y2):
        arr[x2][y], arr[x2][y+1] = arr[x2][y+1], arr[x2][y]
        mn = min(mn, arr[x2][y])
    for x in range(x2, x1, -1):
        arr[x][y2], arr[x-1][y2] = arr[x-1][y2], arr[x][y2]
        mn = min(mn, arr[x][y2])
    for y in range(y2, y1+1, -1):
        arr[x1][y], arr[x1][y-1] = arr[x1][y-1], arr[x1][y]
        mn = min(mn, arr[x1][y])
    return mn
def solution(rows, columns, queries):
    answer = []
    global arr
    arr = [[columns*j + i for i in range(1,columns+1)] for j in range(0,rows)]
    for el in queries:
        x1, y1, x2, y2 = el
        answer.append(rotate(x1-1, y1-1, x2-1, y2-1))
        
    return answer