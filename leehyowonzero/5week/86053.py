def solution(a, b, g, s, w, t):
    start = 0
    end = 10**15
    answer = end

    while start <= end :
        mid = (start + end) // 2
        now_gold = 0
        now_silver = 0
        now_total = 0

        for i in range(len(t)):
            movabletimes = (mid - t[i]) // (t[i] * 2) + 1 # 첫 운반 고려 + 나머지는 왕복이 이루어져야 1번 카운트, 예외상황은 발생하지 않을것으로 판단
            
            # 금으로 다 옮길 때, 최대한 옮길 수 있는 만큼 옮기기
            if (movabletimes * w[i] > g[i]):  # 광물이 부족하니 바닥까지 긁어모아
                now_gold += g[i]
            else: # 광물이 남아...
                now_gold += movabletimes * w[i]
            # 은으로 다 옮길 때, 최대한 옮길 수 있는 만큼 옮기기    
            if (movabletimes * w[i] > s[i]):
                now_silver += s[i]
            else:
                now_silver += movabletimes * w[i]
            # 금 은 상관없이 옮길때, 최대한 옮길 수 있는 만큼 옮기기
            if (s[i] + g[i] < movabletimes * w[i]):
                now_total += s[i] + g[i]
            else:
                now_total += movabletimes * w[i]
                
        if (now_total >= a + b and now_gold >= a and now_silver >= b): # 정해진 시간동안 넉넉하게 광물을 옮길 수 있음
            end = mid - 1 # 시간단축
            answer = min(answer, mid)
        else:
            start = mid + 1 # 시간부족이니 증가

    return answer