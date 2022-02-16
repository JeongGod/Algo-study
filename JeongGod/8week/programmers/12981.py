def solution(n, words):
    answer = [0, 0]
    used = set()
    last = words[0][0]
    for idx, word in enumerate(words):
        # 사용했거나 끝말잇기가 이어지지 않는 경우
        if word in used or last[-1] != word[0]:
            answer = [(idx % n) + 1, (idx // n) + 1]
            break
        used.add(word)
        last = word
    return answer
