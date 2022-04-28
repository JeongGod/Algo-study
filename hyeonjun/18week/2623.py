import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [[] for _ in range(N)]
    cnt = [0 for _ in range(N)]

    for _ in range(M):
        tmp = list(map(int, input().split()))
        for i in range(tmp[0]-1):
            arr[tmp[i+1]-1].append(tmp[i+2])
            cnt[tmp[i+2]-1] += 1

    ans, stack = [], []
    while len(ans) < N:
        for i in range(N):
            if cnt[i] == 0:
                stack.append(i+1)
                cnt[i] = -1
        if stack:
            tmp = stack.pop()
            ans.append(tmp)
            for i in arr[tmp-1]:
                cnt[i-1] -= 1
        else:
            ans = [0]
            break

    for i in ans:
        print(i)
