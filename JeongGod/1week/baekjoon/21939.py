import heapq
import sys

input = sys.stdin.readline

"""
recommend x
    1. x == 1 => 가장 어려운 문제의 번호를 출력한다. 문제 번호가 큰 순으로
    2. x == -1 => 가장 쉬운 문제의 번호를 출력한다. 문제 번호가 작은 순으로
add P L
    1. 난이도가 L인 문제번호 P를 추가한다. 이전에 있던 문제번호가 다른 난이도로 바뀔 수 있다.
solved P
    1. 추천 문제 리스트에서 P를 제거한다. 있는 경우만 주어진다.

1. heapq로 (난이도, 문제의 번호) 순으로 max_heap, min_heap을 구현한다.
2. dict를 사용해 {문제번호 : 난이도} 순으로 정렬한다.
3. solved되었다면 문제번호를 제거한다.
4. recommend를 했을 때 solved되었는지 확인 후 solved되었다면 다음 문제를 출력한다.
"""
N = int(input())

max_hq = []
min_hq = []
problem_dict = dict()


def insert_problem(pro_num, pro_level):
    problem_dict[pro_num] = pro_level
    heapq.heappush(min_hq, (pro_level, pro_num))
    heapq.heappush(max_hq, (-pro_level, -pro_num))


for _ in range(N):
    pro_num, pro_level = map(int, input().split())
    insert_problem(pro_num, pro_level)


M = int(input())
for _ in range(M):
    com, *rest = input().rstrip().split()
    if com == "recommend":
        if rest[0] == "1":
            while True:
                result = problem_dict.get(-max_hq[0][1])
                if result is not None and result == -max_hq[0][0]:
                    break
                heapq.heappop(max_hq)
            print(-max_hq[0][1])
        else:
            while True:
                result = problem_dict.get(min_hq[0][1])
                if result is not None and result == min_hq[0][0]:
                    break
                heapq.heappop(min_hq)
            print(min_hq[0][1])
    elif com == "add":
        insert_problem(int(rest[0]), int(rest[1]))
    elif com == "solved":
        problem_dict.pop(int(rest[0]))
