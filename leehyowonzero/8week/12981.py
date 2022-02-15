def solution(n, words):
    answer = [0,0]
    dictionary = set()
    for i,word in enumerate(words):
        if(i != 0 and word[0] != words[i-1][-1]):
            return [ 1 + i%n, 1 + i//n]
        if(word not in dictionary):
            dictionary.add(word)
        else:
            return [ 1 + i%n, 1 + i//n]

    return answer