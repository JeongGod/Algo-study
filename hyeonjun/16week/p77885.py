from math import floor


def solution(numbers):
    answer = []
    for number in numbers:
        for idx, elm in enumerate(bin(number)[::-1]):
            if elm == '0' or elm == 'b':
                target = floor(2**(idx-1)) ^ number | 2**idx
                answer.append(target)
                break

    return answer
