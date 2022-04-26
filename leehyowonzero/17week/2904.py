def fac(x):
    d = 2 
    while d <= x:
        if (x % d == 0):
            if(d in memo):
                memo[d] += 1
            else:
                memo[d] = 1
                
            x /= d
        else :
            d += 1
def newfac(x):
    nowmemo = dict()
    d = 2 
    while d <= x:
        if (x % d == 0):
            if(d in nowmemo):
                nowmemo[d] += 1
            else:
                nowmemo[d] = 1
                
            x /= d
        else :
            d += 1
    ret = 0
    for key in ans.keys():
        if(key not in nowmemo):
            ret += ans[key]
        else:
            if(ans[key] > nowmemo[key]):
                ret += ans[key]- nowmemo[key]
    return ret

memo = dict()
n  = int(input())
arr = list(map(int, input().split()))
for el in arr:
    fac(el)
    
ans = dict()

for key in memo.keys():
    ans[key] = memo[key] // n
answer = 0
for el in arr:
    answer += newfac(el)

x = 1
for key in ans.keys():
    if(ans[key] !=0):
        for _ in range(ans[key]):
            x *= key

print(x, answer)
