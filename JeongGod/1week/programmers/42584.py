def solution(prices):
    answer = [0] * len(prices)
    """
    0~N-1초를 돌면서 해당 초에 주식가격이 유지될 수 있는지를 판단한다.
    만약 유지되지 못 하고 떨어졌다면 현재 초 - 스택에 있는 초 를 answer로 지정한다.
    유지될 수 있는 때 까지 돈다.
    """
    st = [0]
    for cur_time in range(1, len(prices)):
        
        # 유지되지 못하고 떨어지는 경우
        while st and prices[st[-1]] > prices[cur_time]:
            # 유지되지 못했으니 뽑은 뒤
            target = st.pop()
            # 곧바로 유지 시간을 넣는다.
            answer[target] = cur_time - target
        # 현재 시간을 넣는다.
        st.append(cur_time)

    for idx in st:
        answer[idx] = (len(prices)-1) - idx

    return answer
