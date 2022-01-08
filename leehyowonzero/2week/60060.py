def solution(words, queries):
    wordsBylen = [[] for _ in range(10001)]
    for el in words:
        wordsBylen[len(el)].append(el)
        
    for i in range(len(queries)):
        queries[i] = [queries[i] , len(queries[i])]
        
    answer = [0 for _ in range(len(queries))]
    
    for i, query in enumerate(queries):
        cnt = 0
        if(query[0][0] == '?'):
            value = query[0].split('?')[-1]
            for word in wordsBylen[query[1]]:
                if(word.endswith(value)):
                    cnt += 1
        else:
            value = query[0][:query[0].index('?')]
            # value = query[0].split('?')[0]
            for word in wordsBylen[query[1]]:
                if(word.startswith(value)):
                    cnt += 1
        answer[i] += cnt
    return answer