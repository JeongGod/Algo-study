from itertools import combinations


def minimum_check(val, visited):
    for i in visited:
        if i & val == i:
            return False
    return True

def change_to_bit(com):
    result = 0
    for val in com:
        result ^= 1 << val
    return result

def solution(relation):
    answer = 0
    """
    집합으로 표현했을 때 길이가 같다면 후보키가 가능한 경우
    후보키가 되었다면 방문처리를 하여 해당 친구는 뺀다.
    """
    column = len(relation[0])
    row = len(relation)
    visited = list()
    for i in range(1, column+1):
        for com in combinations(range(column), i):

            # 최소성 만족하는지 체크
            if not minimum_check(change_to_bit(com), visited):
                continue

            candidate_keys = set()  
            # 식별할 수 있는지 체크
            for r in range(row):
                val = ""
                for idx in com:
                    val += relation[r][idx]
                candidate_keys.add(val)
                
            # 식별 가능
            if len(candidate_keys) == row:
                visited.append(change_to_bit(com))
                answer += 1

    return answer
