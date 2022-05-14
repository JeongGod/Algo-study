n = int(input())
A = [[None, None] for _ in range(n)]

for i in range(n):
    A[i][0], A[i][1] = map(int, input().split())

A.sort()
sum_people = 0
for el in A:
    sum_people += el[1]

half_people = sum_people // 2
if(sum_people % 2 == 1):
    half_people += 1
value = 0
for i in range(0, n):
    value += A[i][1]
    if(value >= half_people):
        selected_idx = i
        break
print(A[selected_idx][0])