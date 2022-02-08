import sys

input = sys.stdin.readline

def solution(plans):
    answer = 0
    """
    1. 겹치는건 O(N^2)으로 센다.
    2. 연속되어 있는 것은 end + 1, start를 비교해서 갱신한다.
        1. end + 1 >= start
            => end = start's end
        2. end + 1 < start
            => start = start, end = start's end
    """
    start, end = plans[0][0], plans[0][1]
    col = 0
    for i in range(N):
        gyup = 0
        # 겹치는 횟수를 센다.
        for j in range(i):
            if plans[i][0] <= plans[j][1]:
                gyup += 1
        # 연속되어있는지 판단한다.
        col = max(col, gyup)
        if end + 1 < plans[i][0]:
            # 겹치지 않았으니 계산한다.
            answer += (end - start + 1) * (col + 1)
            start = plans[i][0]
            col = 0
        end = max(end, plans[i][1])
    
    answer += (end - start + 1) * (col + 1)
    return answer
    
if __name__ == "__main__":
    N = int(input())
    plans = sorted([tuple(map(int, input().split())) for _ in range(N)])
    print(solution(plans))
