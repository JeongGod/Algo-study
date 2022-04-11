import sys
from collections import defaultdict

input = sys.stdin.readline

def solution(sushi : list[int], k : int, c : int):
    """
    1. 집합으로 만들어놓는다. 0~k까지
    2. 0은 빼고 k+1번째를 집합에 추가한다.
    3. 해당 집합에다가 쿠폰을 추가한 뒤, 집합 길이의 최댓값을 출력한다.
    """
    cdict = defaultdict(int)
    for i in range(k):
        cdict[sushi[i]] += 1
    ate = set(cdict.keys())
    answer = len(ate)
    if c not in ate:
        answer += 1
    for left in range(len(sushi)):
        right = (left + k) % len(sushi)
        cdict[sushi[left]] -= 1
        cdict[sushi[right]] += 1
        if cdict[sushi[left]] == 0:
            ate.remove(sushi[left])
        ate.add(sushi[right])
        result = len(ate)
        if c not in ate:
            result += 1
        answer = max(answer, result)
        
    return answer

if __name__ == "__main__":
    N, d, k, c = map(int, input().split())
    sushi = [int(input()) for _ in range(N)]
    print(solution(sushi, k, c))
