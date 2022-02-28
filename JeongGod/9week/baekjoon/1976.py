import sys

input = sys.stdin.readline

def find(x : int):
    if x == root[x]:
        return x
    root[x] = find(root[x])
    return root[x]

def union(x : int, y : int):
    if root[x] < root[y]:
        root[x] = root[y]
    else:
        root[y] = root[x]

def solution(cities : list[list[int]], plan : list[int, int, int]):
    global root
    """
    1. 1인 부분은 바꾼다.
    2. 바꿔져 있다면 바꾸지 않는다.
    3. 조상을 찾는다. 같다면 다음 칸, 아니라면 NO
    """
    root = [i for i in range(len(cities))]
    for city_idx in range(len(cities)):
        for idx in range(len(cities)):
            if cities[city_idx][idx] == 1:
                px, py = find(root[idx]), find(city_idx)
                if px == py:
                    continue
                union(px, py)
    
    target = find(root[plan[0]-1])

    for val in plan:
        if target != find(root[val-1]):
            return "NO"
    
    return "YES"


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    cities = [list(map(int, input().split())) for _ in range(N)]
    plan = list(map(int, input().split()))
    print(solution(cities, plan))
