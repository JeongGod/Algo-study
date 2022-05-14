def solution(numbers):
    answer = []
    for number in numbers:
        idx = 2
        if number % 2 == 0: # 짝수
            answer.append(number+1)
            
        else: # 홀수
            tmp = number
            first_idx = 1
            for i in range(len(bin(number)) -1 , 1, -1):
                if (bin(number)[i] == '0'):
                    first_idx = i
                    break
            tmp += 2**(len(bin(number))-1-first_idx)
            for i in range(first_idx+1, len(bin(number))):
                if bin(number)[i] == '1':
                    second_idx = i
                    tmp -= 2**(len(bin(number))-1-second_idx)
                    break
            answer.append(tmp)    
    return answer