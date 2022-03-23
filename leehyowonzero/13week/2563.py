def fill_Map(x, y):
    for i in range(x, x+10):
        for j in range(y, y+10):
            Map[i][j] = True
            
n = int(input())
Map = [[False for _ in range(101)] for _ in range(101)]
for _ in range(n):
    x, y = map(int,input().split())
    fill_Map(x, y)
answer = 0
for i in range(101):
    for j in range(101):
        if(Map[i][j]):
            answer += 1
print(answer)
