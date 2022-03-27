from itertools import permutations
import copy
import pprint
def rotate(arr):   
    nextarr = [[],[]]
    for i in range(3, -1, -1):
        tmp = []
        for j in range(4):
            tmp.append(arr[0][j][i])
        nextarr[0].append(tmp)
    for i in range(3, -1, -1):
        tmp = []
        for j in range(4):
            tmp.append(arr[1][j][i])
        nextarr[1].append(tmp)
    arr = copy.deepcopy(nextarr)
    return nextarr
    
def chagestate(state, mat, x, y):
    for i in range(4):
        for j in range(4):
            state[0][i+x][j+y] += mat[0][i][j]
            if(state[0][i+x][j+y] < 0):
                state[0][i+x][j+y] = 0
            elif(state[0][i+x][j+y] > 9):
                state[0][i+x][j+y] = 9
                
            if(mat[1][i][j] != 'W'):
                state[1][i+x][j+y] = mat[1][i][j]
    return state
def calc_quality(arr):
    R = 0
    B = 0
    G = 0
    Y = 0
    for i in range(5):
        for j in range(5):
            if(arr[1][i][j] == 'R'):
                R += arr[0][i][j]
            elif(arr[1][i][j] == 'B'):
                B += arr[0][i][j]
            elif(arr[1][i][j] == 'G'):
                G += arr[0][i][j]
            elif(arr[1][i][j] == 'Y'):
                Y += arr[0][i][j]
    return 7*R + 5*B + 3*G + 2*Y
    
def dfs(perm, state, cnt):
    global answer
    if(cnt == 3):
        ret = calc_quality(state)
        answer = max(ret, answer)
        return 
    nowmaterial = material[perm[cnt]]
    for d in range(4):
        rotatedmaterial = rotate(nowmaterial)
        for i in range(0, 2):
            for j in range(0, 2):
                nowstate = copy.deepcopy(state)
                nextstate = chagestate(nowstate, rotatedmaterial, i, j)
                dfs(perm, nextstate, cnt +1)
        nowmaterial = rotatedmaterial
        
answer = 0
n = int(input())
material = [[[], []] for _ in range(n)] # i 번째 재료의[효능, 원소]
for i in range(n):
    for _ in range(4):
        material[i][0].append(list(map(int,input().split())))
    for _ in range(4):
        material[i][1].append(list(input().split()))
kiln = [[[0 for _ in range(5)] for _ in range(5)], [['W' for _ in range(5)]for _ in range(5)]]

materidx = [i for i in range(n)]
for perm in list(permutations(materidx, 3)):
    dfs(perm, kiln, 0)
print(answer)