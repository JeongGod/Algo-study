
def check(candi):
    ret = max(candi) - min(candi)
    idx = candi.index(min(candi))    
    return ret, idx

n, m = map(int,input().split())
arr = []
answer = 10**9 + 1
for _ in range(n):
    thisclass = list(map(int,input().split()))
    thisclass.sort()
    arr.append(thisclass)
selected_idx = [0 for _ in range(n)]
candi = []
for i in range(n):
    candi.append(arr[i][selected_idx[i]])
while True:
    value, min_idx = check(candi)
    answer = min(answer, value)
    selected_idx[min_idx] += 1
    if(selected_idx[min_idx] >= m):
        break
    candi[min_idx] = arr[min_idx][selected_idx[min_idx]]
print(answer)