def Plus(arr_x, arr_y):
    ret = []
    for x in arr_x:
        for y in arr_y:
            tmp = x + y
            ret.append(tmp)
    return ret

def Minus(arr_x, arr_y):
    ret = []
    for x in arr_x:
        for y in arr_y:
            tmp = abs(x - y)
            ret.append(tmp)
    return ret

def Multiple(arr_x, arr_y):
    ret = []
    for x in arr_x:
        for y in arr_y:
            tmp = x * y
            ret.append(tmp)
    return ret

def Divide(arr_x, arr_y):
    ret = []
    for x in arr_x:
        for y in arr_y:
            if(y == 0):
                continue
            tmp = x // y
            ret.append(tmp)
    return ret
    
def solution(N, number):
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N)*i))
        for k in range(1, i):
            for el in Plus(dp[k], dp[i-k]):
                dp[i].add(el)
            for el in Minus(dp[k], dp[i-k]):
                dp[i].add(el)
            for el in Multiple(dp[k], dp[i-k]):
                dp[i].add(el)
            for el in Divide(dp[k], dp[i-k]):
                dp[i].add(el)
    for i in range(1, 9):
        if(number in dp[i]):
            return i
    return -1