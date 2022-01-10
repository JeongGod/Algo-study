import sys

sys.setrecursionlimit(10 ** 6)


def order(info, result, flag):  # flag 0 : pre_order, 1: post_order
    if len(info) == 0:
        return result
    if len(info) == 1:
        result.append(tree[tuple(info[0])])
        return result
    max_idx = info.index(max(info, key=lambda x: x[1]))
    if not flag:
        result.append(tree[tuple(info[max_idx])])
        order(info[:max_idx], result, 0)
        order(info[max_idx + 1 :], result, 0)
    else:
        order(info[:max_idx], result, 1)
        order(info[max_idx + 1 :], result, 1)
        result.append(tree[tuple(info[max_idx])])
    return result


def solution(nodeinfo):
    global tree
    tree = {tuple(val): idx + 1 for idx, val in enumerate(nodeinfo)}
    nodeinfo.sort()
    return [order(nodeinfo, [], 0), order(nodeinfo, [], 1)]
