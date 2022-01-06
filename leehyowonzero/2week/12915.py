def solution(strings, n):
    strings.sort() # n번 인덱스가 동일 시 사전순으로 정렬하기 위하여 미리 사전순 정렬 실시
    strings.sort(key = lambda x : x[n]) # 문제에서 요구하는 n번 인덱스 기준 정렬
    return strings