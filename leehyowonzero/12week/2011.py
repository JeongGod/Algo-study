n = input()
if(len(n) == 0 or n[0] == '0'):
    print(0)
    exit(0)
if(len(n) == 1):
    print(1)
    exit(0)
dp = [0 for _ in range(len(n))]
dp[0] = 1
if(int(n[0:2]) <= 26):
    if(n[1] != '0'):
        dp[1] = 2
    else:
        dp[1] = 1
else:
    if(n[1] != '0'):
        dp[1] = 1
    else:
        print(0)
        exit(0)

for i in range(2, len(n)):
    if(n[i] == '0'):
        if(int(n[i-1]) > 2 or n[i-1] == '0'): # 망한케이스
            print(0)
            exit(0)
        else:
            dp[i] = dp[i-2]
    else:
        if(int(n[i-1:i+1]) <= 26 and n[i-1] != '0'):
            dp[i] = dp[i-1] + dp[i-2]
        else:
            dp[i] = dp[i-1]
            
        
print(dp[len(n)-1] % 1000000)
