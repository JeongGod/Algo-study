def check():
    checkline = [[spotpos[0], spotpos[2], spotpos[5], spotpos[7]],[spotpos[0], spotpos[3], spotpos[6], spotpos[10]],[spotpos[1], spotpos[2], spotpos[3], spotpos[4] ],[spotpos[1], spotpos[5], spotpos[8], spotpos[11]],[spotpos[4], spotpos[6], spotpos[9], spotpos[11]],[spotpos[7], spotpos[8], spotpos[9], spotpos[10]]]
    for i in range(6): 
        flag = False
        sm = 0
        for x, y in checkline[i]:
            if(Map[x][y] == 'x'):
                flag = True
                break
            sm += ord(Map[x][y]) - 64
        if(not flag and sm != 26):
            return False
            
    return True       

def dfs(cnt):
    if(check() == False):
        return False
    if(cnt == len(checkpos)):
        return True

    for i in range(12):
        if(visited[i] != True):
            Map[checkpos[cnt][0]][checkpos[cnt][1]] = chr(i + 65)
            visited[i] = True
            if( dfs(cnt + 1)):
                return True
            Map[checkpos[cnt][0]][checkpos[cnt][1]] = 'x'
            visited[i] = False
            
Map = []
for _ in range(5):
    Map.append(list(input()))
visited = [False for _ in range(12)]
spotpos = [(0, 4), (1, 1), (1, 3), (1, 5), (1, 7), (2, 2), (2, 6), (3, 1), (3, 3), (3, 5), (3, 7), (4, 4)]
checkpos = []
for x, y in spotpos:
    if(Map[x][y] == 'x'): # 비어 있음
        checkpos.append([x, y])
    else:
        visited[ord(Map[x][y]) - 65] = True

dfs(0)

for i in range(5):
    print(''.join(Map[i]))