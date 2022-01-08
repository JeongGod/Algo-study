import sys
from typing import List, Tuple

sys.setrecursionlimit(10000)


def split(nodes: List[List[int]]) -> Tuple[int, List[List[int]], List[List[int]]]:
    rootx, _, root = max(nodes, key=lambda x: x[1])
    left = list(filter(lambda x: x[0] < rootx, nodes))
    right = list(filter(lambda x: x[0] > rootx, nodes))
    return root, left, right


def preorder(nodes: List[List[int]]) -> List[int]:
    if not nodes:
        return []
    root, left, right = split(nodes)
    return [root] + preorder(left) + preorder(right)


def postorder(nodes: List[List[int]]) -> List[int]:
    if not nodes:
        return []
    root, left, right = split(nodes)
    return postorder(left) + postorder(right) + [root]


def solution(nodeinfo: List[List[int]]) -> List[List[int]]:
    nodes = [[x, y, idx + 1] for idx, [x, y] in enumerate(nodeinfo)]
    return [preorder(nodes), postorder(nodes)]


# [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
print(
    solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]])
)
