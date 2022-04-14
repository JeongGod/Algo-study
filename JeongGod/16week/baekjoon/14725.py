import sys

input = sys.stdin.readline

class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}

def search(cur, depth):
    for key in sorted(cur.children.keys()):
        child = cur.children.get(key)
        if child is None:
            continue
        print("-"*depth + child.val)
        search(child, depth+2)
        

if __name__ == "__main__":
    N = int(input())
    root = Node(None)

    for _ in range(N):
        k, *nodes = input().rstrip().split()
        cur = root
        for i in range(int(k)):
            if nodes[i] in cur.children:
                cur = cur.children[nodes[i]]
                continue
            tmp = Node(nodes[i])
            cur.children[nodes[i]] = tmp
            cur = tmp
    
    search(root, 0)
