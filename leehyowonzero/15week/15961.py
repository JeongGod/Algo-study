n, d, k, c = map(int, input().split())
answer = 0
arr = []
for _ in range(n):
    arr.append(int(input()))

arr = arr + arr[:k-1]
selected_idx = [0 for _ in range(d+1)]
selected_idx[c] += 1

for i in range(0, k):
    selected_idx[arr[i]] += 1 

for i in range(0, d+1):
    if(selected_idx[i] != 0):
        answer += 1
nowmax = answer
for start_idx in range(1, n):
    selected_idx[arr[start_idx -1 ]] -= 1
    if(selected_idx[arr[start_idx -1 ]] == 0):
        nowmax -= 1
    if(selected_idx[arr[start_idx -1 + k]] == 0):
        nowmax += 1
    selected_idx[arr[start_idx -1 + k]] += 1
    answer = max(answer, nowmax)

print(answer)
    