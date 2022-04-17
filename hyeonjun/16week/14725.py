import sys
input = sys.stdin.readline


class Trie():
    def __init__(self):
        self.head = {}

    def insert(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node:
                curr_node[char] = {}
            curr_node = curr_node[char]
        curr_node[0] = True

    def travel(self, level, curr_node):
        if 0 in curr_node:
            return 0
        cur_child = sorted(curr_node)
        for child in cur_child:
            print("--" * level + child)
            self.travel(level+1, curr_node[child])


if __name__ == "__main__":
    trie = Trie()
    N = int(input())
    for _ in range(N):
        info = list(input().split())
        trie.insert(info[1:])

    trie.travel(0, trie.head)
