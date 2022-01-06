def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    for i in numbers:
        if(i == 1 or i == 4 or i == 7 ):
            answer += 'L'
            left = i
        elif(i == 3 or i == 6 or i == 9 ):
            answer += 'R'
            right = i
        else:
            if i == 0:
                i = 11
            ld = abs(i-left)//3 + abs(i-left)%3
            rd = abs(i-right)//3 + abs(i-right)%3
            if (ld == rd):
                if(hand == 'right'):
                    answer += 'R'
                    right= i
                else:
                    answer += 'L'
                    left= i
            else:
                if(ld < rd):
                    answer += 'L'
                    left= i
                else:
                    answer += 'R'
                    right= i
            
    return answer