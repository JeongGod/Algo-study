import sys
input = sys.stdin.readline


if __name__ == "__main__":
    def noon(survivor, cnt):
        global night_cnt, flag
        if flag:
            return 0

        if survivor == 1:
            night_cnt = max(night_cnt, cnt)
            flag = True
            return 0

        tmp = -1
        candidate = 0
        for idx in range(N):
            if dead[idx]:
                continue
            if guilty_index[idx] > tmp:
                candidate = idx
                tmp = guilty_index[idx]

        if candidate == eunjin:
            night_cnt = max(night_cnt, cnt)
            return 0

        dead[candidate] = 1
        night(survivor-1, cnt)
        dead[candidate] = 0

    def night(survivor, cnt):
        global night_cnt
        if flag:
            return 0

        for idx in range(N):
            if idx == eunjin or dead[idx]:
                continue

            dead[idx] = 1
            for i in range(N):
                guilty_index[i] += R[idx][i]

            noon(survivor-1, cnt+1)

            dead[idx] = 0
            for i in range(N):
                guilty_index[i] -= R[idx][i]

    N = int(input())
    guilty_index = list(map(int, input().split()))
    R = [list(map(int, input().split())) for _ in range(N)]
    eunjin = int(input())
    dead = [0 for _ in range(N)]
    night_cnt = 0
    flag = False

    if N % 2:
        noon(N, 0)
    else:
        night(N, 0)

    print(night_cnt)
