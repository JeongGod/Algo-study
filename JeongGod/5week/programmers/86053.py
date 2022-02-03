import math


def solution(a, b, g, s, w, t):
    """
    a 금, b 은 만큼 필요
    i번 도시 : g[i] 금, s[i] 은, t[i] 편도 시간걸림, w[i]만큼 광물 운반 가능
    
    최적으로 운행했을 때 가장 빠른 시간을 구해라.
    도시에 트럭이 하나씩 다 있는 거였음..
    """
    answer = 2*1e5 * 2*1e9
    left = 0
    right = 2*1e5 * 2*1e9
    while left <= right:
        mid = (left + right) // 2
        tgold, tsilver, tgs = 0, 0, 0
        # 해당 mid만큼 도시에서 운반할 수 있는 양을 구한다.
        for gold, silver, weight, time in zip(g, s, w, t):
            # 편도로 한 번 더 올 수 있는지 확인
            # go = round(mid / (time*2)) # => 0.5를 반올림 못함
            go = mid / (time * 2)
            go = math.ceil(go) if (go * 10) % 10 >= 5 else math.floor(go)
            tgold += gold if go*weight > gold else go*weight
            tsilver += silver if go*weight > silver else go*weight
            tgs += gold+silver if go*weight > gold+silver else go*weight

        if tgold >= a and tsilver >= b and tgs >= a+b:
            right = mid-1
            if answer > mid:
                answer = mid
        else:
            left = mid+1
    return answer
