def solution(strings, n):
    strings.sort()  # n번째 문자가 같은 문자열이 존재할 경우를 대비해 미리 사전순으로 정렬
    strings.sort(key=lambda x: x[n])  # n번째 문자를 기준으로 오름차순 정렬
    return strings
