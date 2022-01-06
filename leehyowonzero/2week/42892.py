import sys
sys.setrecursionlimit(10**6)

def preorder(rootTree): # 전위순회
    global preorderedlist
    preorderedlist.append(rootTree.root[0])
    if rootTree.leftnodelist :
        preorder(Tree(rootTree.leftnodelist))
    if rootTree.rightnodelist:
        preorder(Tree(rootTree.rightnodelist))
        
def postorder(rootTree): # 후위순회
    global postorderlist
    if rootTree.leftnodelist :
        postorder(Tree(rootTree.leftnodelist))
    if rootTree.rightnodelist:
        postorder(Tree(rootTree.rightnodelist))
    postorderlist.append(rootTree.root[0])

class Tree:
    def __init__(self, nodelist):
        self.root = max(nodelist, key = lambda x : x[2]) # 가장 y 좌표값이 높은 node => root node
        self.leftnodelist = nodelist[ :nodelist.index(self.root)] # root node idx 기준으로 좌측 node
        self.rightnodelist = nodelist[nodelist.index(self.root)+1: ] # root node idx 기준으로 우측 node
        

def solution(nodeinfo):
    global preorderedlist, postorderlist
    preorderedlist = []
    postorderlist = []
    nodelist = [] # [[nodeidx, x, y], ...]
    for i, el in enumerate(nodeinfo):
        nodelist.append([i+1, *el])
    nodelist.sort(key = lambda x : x[1]) # x 좌표를 기준으로 정렬
    rootTree = Tree(nodelist)
    preorder(rootTree) # 전위순회
    postorder(rootTree) # 후위순회
    
    answer = []
    answer.append(preorderedlist)
    answer.append(postorderlist)
    return answer