import sys
input = sys.stdin.readline

# 수가 3개이상일 때 경우의수 2개, 1개일때 경우의 수를 분류
# 홀수인지 판단 -> 문자열 이용해서 


def count_odd(string) -> int:
    cnt = 0
    for i in string:
        if int(i) % 2 == 1:
            cnt += 1
    return cnt


def dfs(N, cnt) -> None:
    global min_v, max_v
    cnt = cnt + count_odd(N)

    if len(N) == 1:
        min_v = min(min_v, cnt)
        max_v = max(max_v, cnt)
        return
    elif len(N) == 2:
        N = str(int(N)//10 + int(N) % 10)
        dfs(N, cnt)
    else:
        for i in range(1, len(N)):
            for j in range(i+1, len(N)):
                new_N = str(int(N[:i]) + int(N[i:j]) + int(N[j:]))
                dfs(new_N, cnt)


if __name__ == "__main__":
    N = str(input().rstrip())
    min_v = sys.maxsize
    max_v = 0

    dfs(N, 0)
    print(min_v, max_v)
