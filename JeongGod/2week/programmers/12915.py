def solution(strings, n):
    return sorted(sorted(strings), key=lambda x:x[n])