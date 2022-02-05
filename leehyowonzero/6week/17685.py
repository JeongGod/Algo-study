class Node(object):
    def __init__(self, data):
        self.data = data
        self.count = 0
        self.child = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        cur = self.head
        cur.count += 1
        
        for c in string:
            if c not in cur.child:
                cur.child[c] = Node(c)
            cur = cur.child[c]
            cur.count += 1
    
    def count(self, prefix):
        cur = self.head
        
        for c in prefix:
            if(cur.count == 1):
                return True
            cur = cur.child[c]
        return False
    
def solution(words):
    answer = 0
    word_trie = Trie()
    
    for word in words:
        word_trie.insert(word)
    
    for word in words:
        cnt = len(word)
        for i in range(0, len(word)):
            if(word_trie.count(word[0:i+1]) == True):
                cnt = i
                break
        answer += cnt
    
    return answer