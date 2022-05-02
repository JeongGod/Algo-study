from collections import defaultdict


def solution(n, wires):
    def search(node1, node2, cnt):
        for node in grid[node1]:
            if node != node2:
                cnt += search(node, node1, 1)
        return cnt

    answer = n
    grid = defaultdict(list)
    for node1, node2 in wires:
        grid[node1].append(node2)
        grid[node2].append(node1)

    for node1, node2, in wires:
        answer = min(answer, abs(n-2*search(node1, node2, 1)))

    return answer
