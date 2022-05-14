n = int(input())
m = int(input())
answer = abs(100 - n)
if m != 0:
    wrongkey = set(list(map(str, input().split())))
    
    for num in range(0, 1000001):
        flag = False
        for el in str(num):
            if(el in wrongkey):
                flag = True
                break
        if not (flag):
            answer= min(answer, len(str(num)) + abs(n - num))
                
    
else:
    answer = min(answer, len(str(n)))

print(answer)