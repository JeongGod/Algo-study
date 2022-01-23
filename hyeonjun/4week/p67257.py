import re
from itertools import permutations
from copy import deepcopy


def calc(arr, target, start):
    for idx, sign in enumerate(arr[start:]):
        idx += start
        if target == sign:
            arr[idx-1] = eval(
                str(arr[idx-1]) + sign + str(arr[idx+1]))
            del arr[idx]
            del arr[idx]
            calc(arr, sign, idx-1)
            return 0
    return 1


def solution(expression):
    answer = 0
    signs = set(re.findall('[-+*]', expression))
    test = re.split('\D', expression)

    signs_comb = permutations(signs, len(signs))

    for order in signs_comb:
        copy_numbers = deepcopy(test)
        for target in order:
            calc(copy_numbers, target, 0)
        if answer < abs(copy_numbers[0]):
            answer = abs(copy_numbers[0])
    return answer
