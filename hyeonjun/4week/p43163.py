from collections import deque


def bfs(begin, target):
    queue = deque()
    queue.append((begin, 0))
    while queue:
        letter_idx, cnt = queue.popleft()
        for word in tree[letter_idx]:
            if word == target:
                return cnt+1
            if not visited[word]:
                queue.append((word, cnt+1))
    return 0


def compare_words(word1, word2):
    different_cnt = 0
    for idx, letter in enumerate(word1):
        if letter != word2[idx]:
            different_cnt += 1
        if different_cnt > 1:
            return 0
    return 1


def make_tree(words):
    length = len(words)
    for i in range(length):
        for j in range(i+1, length):
            if compare_words(words[i], words[j]):
                tree[i].append(j)
                tree[j].append(i)
    return 1


def solution(begin, target, words):
    global tree
    global visited

    if target not in words:
        return 0

    length = len(words)
    tree = {i: [] for i in range(length+2)}
    visited = [0 for _ in range(length+2)]

    words.append(begin)
    words.append(target)

    make_tree(words)

    return bfs(length, length+1)
