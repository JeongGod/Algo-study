from math import gcd

def solution(w,h):
    pattern_num = gcd(w,h)
    pattern_w = w/pattern_num
    pattern_h = h/pattern_num
    answer = w * h - pattern_num * (pattern_w + pattern_h - 1)
    return answer