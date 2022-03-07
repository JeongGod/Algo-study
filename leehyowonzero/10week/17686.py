def solution(files):
    answer = []
    arr = []
    for el in files:
        for i in range(len(el)):
            if(el[i].isdigit()):
                head = el[:i]
                numberstart = el[i:]
                break
        flag = True
        for i in range(len(numberstart)):
            if not (numberstart[i].isdigit()):
                number = numberstart[:i]
                tail = numberstart[i:]
                flag = False
                break
        if(flag):
            number = numberstart
            tail = ''
        arr.append((head, number, tail))
    arr.sort(key = lambda x : (x[0].lower(), int(x[1])))
    for el in arr:
        answer.append(''.join(el))
    return answer