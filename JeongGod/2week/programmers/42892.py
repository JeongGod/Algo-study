import sys
sys.setrecursionlimit(10000)
class Tree:
    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None

    def insert_left(self, node):
        self.left = node

    def insert_right(self, node):
        self.right = node

class Node:
    def __init__(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y

def solution(nodeinfo):
    answer = [[], []]
    nodes = []
    # 노드들의 번호까지 함께 있게 바꾼다. [(x, y), idx]
    for idx, (x, y) in enumerate(nodeinfo, start=1):
        nodes.append(((x, y), idx))
    nodes = sorted(nodes, key=lambda x: (x[0][1], -x[0][0]))


    def dfs(a):
        # 해당 노드를 answer[0]에 넣는다.
        if a is None:
            return
        answer[0].append(a.node.num)
        # node 보다 y좌표는 작고, x좌표도 작은 곳을 탐사한다.
        # node 보다 y좌표는 작고, x좌표는 큰 곳을 탐사한다.
        dfs(a.left)
        dfs(a.right)

        # 해당 노드를 answer[1]에 넣는다.
        answer[1].append(a.node.num)

    node = Node(nodes[-1][1], nodes[-1][0][0], nodes[-1][0][1])
    root = Tree(node)

    def make_tree(root, x, y, node_num):
        if x < root.node.x and y < root.node.y:
            if root.left is None:
                node = Node(node_num, x, y)
                root.insert_left(Tree(node))
            else:
                make_tree(root.left, x, y, node_num)
        elif x > root.node.x and y < root.node.y:
            if root.right is None:
                node = Node(node_num, x, y)
                root.insert_right(Tree(node))
            else:
                make_tree(root.right, x, y, node_num)

    for idx in range(len(nodes)-2, -1, -1):
        (cx, cy), node_num = nodes[idx]
        make_tree(root, cx, cy, node_num)


    # 루트노드부터 들어가자.
    dfs(root)

    return answer