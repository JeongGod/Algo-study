from collections import deque


def solution(relations):
    answer = []
    targets = deque()
    targets.append([i for i in range(len(relations[0]))])

    while targets:
        check = 0
        target = targets.popleft()
        for i in range(len(target)):
            sum_list = []
            for leng in range(len(relations)):
                copy_target = target.copy()
                copy_target.remove(target[i])
                tuple_sum = ''
                for key_idx in copy_target:
                    tuple_sum += relations[leng][key_idx]
                sum_list.append(tuple_sum)

            if (len(set(sum_list)) == len(sum_list)) and (copy_target not in targets):
                targets.append(copy_target)
            elif (len(set(sum_list)) != len(sum_list)):
                check += 1

        if check == len(target):
            answer.append(target)

    return len(answer)
