def solution(n, words):
    answer = [0, 0]
    store = set()
    store_length = 0
    pri_word = words[0][0]

    for idx, word in enumerate(words):
        store.add(word)
        store_length += 1
        if store_length != len(store) or word[0] != pri_word:
            if (idx+1) % n:
                answer = [(idx+1) % n, (idx+1)//n+1]
            else:
                answer = [n, (idx+1)//n]
            break
        pri_word = word[-1]

    return answer
