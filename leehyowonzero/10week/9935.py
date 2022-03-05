from collections import deque

string = input()
boom = input()

q = deque()
for el in string:
    q.append(el)
    if len(q) >= len(boom) and q[-1] == boom[-1]:
        for i in range(len(boom)):
            if(boom[len(boom) - 1 - i] == q[-1-i]):
                if(i == len(boom)-1):
                    for _ in range(len(boom)):
                        q.pop()
                continue
            else:
                break
answer = ''.join(list(q))
if answer:
    print(answer)
else:
    print("FRULA")