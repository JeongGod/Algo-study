n = int(input())
crain = list(map(int, input().split()))
m = int(input())
boxs = list(map(int, input().split()))
crain.sort(reverse = True)
boxs.sort(reverse = True)

if(crain[0] < boxs[0]):
    print(-1)
    exit(0)
time = 0
while True:
    flag = False
    for crain_idx in range(0, n):
        for i in range(len(boxs)):
            if(crain[crain_idx] >= boxs[i]):
                flag = True
                del boxs[i]
                break
    if not(flag):
        break
    time += 1

print(time)