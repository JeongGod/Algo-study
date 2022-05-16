import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    
    villages = sorted([list(map(int, input().split())) for _ in range(N)])

    ans = sum(people for pos, people in villages)
    if ans % 2 == 1:
        ans = (ans+1) // 2
    else:
        ans //= 2

    cnt = 0
    for pos, people in villages:
        cnt += people
        if cnt >= ans:
            print(pos)
            break
