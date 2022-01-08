from collections import defaultdict
from typing import DefaultDict, Dict, List


class Node:
    def __init__(self, key: str) -> None:
        self.key = key
        self.children: Dict[str, Node] = {}
        self.numofchildren: int = 0


class Trie:
    def __init__(self) -> None:
        self.root = Node("")

    def insert(self, string: str) -> None:
        cur: Node = self.root
        for char in string:
            if char not in cur.children:
                cur.children[char] = Node(char)
            cur.numofchildren += 1
            cur = cur.children[char]

    def search(self, string: str) -> int:
        cur: Node = self.root
        for char in string:
            if char == "?":
                return cur.numofchildren
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return 0


def reverse(string: str) -> str:
    return "".join(reversed(string))


def startswithqm(string: str) -> bool:
    return string[0] == "?" and string[-1] != "?"


def solution(words: List[str], queries: List[str]) -> List[int]:
    tries: DefaultDict[int, Trie] = defaultdict(Trie)
    rtries: DefaultDict[int, Trie] = defaultdict(Trie)

    for word in words:
        length: int = len(word)
        tries[length].insert(word)
        rtries[length].insert(reverse(word))

    answer: List[int] = []
    for query in queries:
        length: int = len(query)
        if startswithqm(query):
            answer.append(rtries[length].search(reverse(query)))
        else:
            answer.append(tries[length].search(query))
    return answer


# [3, 2, 4, 1, 0]
print(
    solution(
        ["frodo", "front", "frost", "frozen", "frame", "kakao"],
        ["fro??", "????o", "fr???", "fro???", "pro?"],
    )
)
