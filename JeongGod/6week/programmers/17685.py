import sys

sys.setrecursionlimit(1000000)
class Node:
    def __init__(self):
        self.child = [None] * 26
        self.num = 0

    def insert_node(self, val, depth):
        if depth == len(val):
            return
        cur = ord(val[depth]) - ord('a')

        if not self.child[cur]:
            self.child[cur] = Node()
        self.child[cur].num += 1
        self.child[cur].insert_node(val, depth+1)

    def find_node(self, val, depth):
        if depth == len(val) or self.num == 1:
            return depth

        cur = ord(val[depth]) - ord('a')
        return self.child[cur].find_node(val, depth+1)
class Trie:
    def __init__(self, node):
        self.root = node

def solution(words):
    answer = 0
    root = Node()
    trie = Trie(root)
    for word in words:
        trie.root.insert_node(word, 0)

    for word in words:
        result = trie.root.find_node(word, 0)
        answer += result
        
    return answer
