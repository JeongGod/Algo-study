import sys
from itertools import combinations

MIN_VAL = sys.maxsize
MAX_VAL = 0
input = sys.stdin.readline

def calc_odd(n):
    return len(list(filter(lambda x: int(x)%2 == 1, n)))

def solution(n : str, answer : int): 
    global min_ans, max_ans
    if len(n) >= 3:
        for start, end in combinations(range(len(n)-1), 2):
            a, b, c = n[:start+1], n[start+1:end+1], n[end+1:]
            result = f"{sum(map(int, [a, b, c]))}"
            solution(result, answer + calc_odd(result))
    elif len(n) == 2:
        result = f"{sum(map(int, n))}"
        solution(result, answer + calc_odd(result))
    else:
        min_ans = min(answer, min_ans)
        max_ans = max(answer, max_ans)
        return
    


if __name__ == "__main__":
    N = input().rstrip()
    min_ans = MIN_VAL
    max_ans = MAX_VAL
    solution(N, calc_odd(N))
    print(min_ans, max_ans)
