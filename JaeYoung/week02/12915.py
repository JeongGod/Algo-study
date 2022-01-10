def solution(strings, n):
    index_list = []
    answer = []
    
    for x in strings: # strings 원소의 n번째 문자 추출
        index_list.append(x[n])
        
    index_list.sort() 
    strings.sort()
    
    for index in index_list: # 정렬한 index_list, strings 를 통해 n번째 문자 비교
        for x in strings[:]:
            if x[n] == index:
                answer.append(str(x))
                strings.remove(x)
                break
    
    return answer