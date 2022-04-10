n, w = map(int,input().split())
check = [0 for _ in range(n+1)]
for _ in range(n-1):
    fm , to = map(int,input().split())
    check[fm] += 1
    check[to] += 1
anscnt = 0
for i in range(2, n+1):
    if(check[i] == 1):
        anscnt += 1
print(w/anscnt)