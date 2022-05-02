import sys
input = sys.stdin.readline


def choose(start_idx, start, cnt):
    global ans
    if cnt >= L and difficulties[start_idx-1] - start >= X:
        ans += 1

    for idx, difficulty in enumerate(difficulties[start_idx:]):
        if not start:
            choose(idx+1, difficulty, difficulty)

        else:
            tmp = cnt + difficulty
            if tmp <= R:
                choose(start_idx+idx+1, start, tmp)
            else:
                break


if __name__ == "__main__":
    ans = 0
    N, L, R, X = map(int, input().split())
    difficulties = list(map(int, input().split()))
    difficulties.sort()
    choose(0, 0, 0)
    print(ans)
