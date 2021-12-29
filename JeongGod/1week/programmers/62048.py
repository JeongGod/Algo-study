def solution(w, h):
    answer = 1
    """
    ans = w*h - (w+h - 최대공약수)
    """

    x, y = max(w, h), min(w, h)
    while True:
        tmp = x % y
        if tmp == 0:
            break
        x, y = y, tmp
    # y의 값이 최대공약수

    return w * h - (w + h - y)
