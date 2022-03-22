def solution(n):
    answer = [[None for _ in range(n)] for _ in range(n)]
    ret = []
    nowlen = n
    row = -1
    col = 0
    idx = 1
    for turn in range(n):    
        if(turn % 3 == 0): # 밑으로 내리기 
            for _ in range(nowlen):
                row += 1
                answer[row][col] = idx
                idx += 1
        elif(turn % 3 == 1): # 오른쪽으로 밀기
            for _ in range(nowlen):
                col += 1
                answer[row][col] = idx
                idx += 1
        elif(turn % 3 == 2): # 왼쪽 윗 대각선으로 올라오기
            for _ in range(nowlen):
                row -= 1
                col -=1
                answer[row][col] = idx
                idx += 1
                
        nowlen -= 1
    for i in range(n):
        for el in answer[i]:
            if el != None:
                ret.append(el)
            else:
                break
    return ret