import sys
sys.setrecursionlimit(10000) #재귀 제한 설정

preorder_list = []
postorder_list = []

class Node: #노드 객체 클래스
    def __init__(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y
        self.left = None
        self.right = None
    

def preorder(node): #전위 순회
    preorder_list.append(node.num)
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)
        
def postorder(node): #후위 순회
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    postorder_list.append(node.num)
    

def solution(nodeinfo):
    nodes = {}
    node_list = []
    
    for i in range(len(nodeinfo)):
        x, y = nodeinfo[i]
        nodeinfo[i].append(i+1)

        
    nodes = sorted(nodeinfo, key=lambda x: (-x[1], x[0])) # y는 내림차순, x는 올림차순으로 정렬
    
    # print(nodes)
    
    
    #최상위 루트 노드 추가
    root = Node(nodes[0][2], nodes[0][0], nodes[0][1])
    
    for node in nodes[1:]:
        cur_node = root #현재 기준 노드를 최상위 루트 노드로 설정
        next_x, next_y, next_num = node
        while True:
            if cur_node.x > next_x: # 현재 기준 노드보다 왼쪽에 있는 경우
                if cur_node.left: #현재 기준 노드 왼쪽 자식이 있으면 기준 노드를 왼쪽 자식으로 설정
                    cur_node = cur_node.left #
                    continue
                else: #현재 기준 노드 왼쪽 자식이 없으면 추가
                    cur_node.left = Node(next_num, next_x, next_y)
                    break
            elif cur_node.x < next_x: #현재 기준 노드보다 오른쪽에 있는 경우
                if cur_node.right: #현재 기준 노드 오른쪽 자식이 있으면 기준 노드를 오른쪽 자식으로 설정
                    cur_node = cur_node.right
                    continue
                else: #현재 기준 노드 오른쪽 자식이 없으면 추가
                    cur_node.right = Node(next_num, next_x, next_y)
                    break
                    
    preorder(root)
    postorder(root)
    
    return [preorder_list, postorder_list]