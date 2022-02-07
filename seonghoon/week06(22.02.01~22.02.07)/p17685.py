from typing import Dict, List


class Node:
    def __init__(self, char: str) -> None:
        self.char: str = char
        self.num: int = 0
        self.children: Dict[str, Node] = {}


class Trie:
    def __init__(self) -> None:
        self.root: Node = Node("")

    def insert(self, word: str) -> None:
        node: Node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]
            node.num += 1

    def search(self, word: str) -> int:
        num: int = 0
        node: Node = self.root
        for char in word:
            node = node.children[char]
            num += 1
            if node.num == 1:
                break
        return num


def solution(words: List[str]) -> int:
    trie: Trie = Trie()
    for word in words:
        trie.insert(word)

    answer: int = 0
    for word in words:
        answer += trie.search(word)
    return answer


# 7
print(solution(["go", "gone", "guild"]))
# 4
print(solution(["abc", "def", "ghi", "jklm"]))
# 15
print(solution(["word", "war", "warrior", "world"]))
