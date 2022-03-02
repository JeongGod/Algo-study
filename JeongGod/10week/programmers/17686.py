import re


def solution(files):
    """
    1. HEAD부분을 기준으로 사전 순 정렬(대소문자 구분 X)
    2. NUMBER의 숫자순으로 정렬
    3. 같을 경우 주어진 순서 유지
    """
    answer = []
    pattern = re.compile("[0-9]+")
    
    for idx, file in enumerate(files):
        num_idx = pattern.search(file)
        
        start, end = num_idx.start(), num_idx.end()
        name = file[:start].lower()
        number = int(file[start:end])
        
        answer.append((name, number, idx))
    answer.sort(key=lambda x: (x[0], x[1]))
    return list(files[idx] for _, _, idx in answer)
