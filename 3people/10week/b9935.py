word = input()
explode = input()
stack = []

for i in range(len(word)):
  stack.append(word[i])
  if len(stack) >= len(explode):
    temp = "".join(stack[len(stack) - len(explode):])
    if temp == explode:
      for i in range(len(temp)):
        stack.pop()

if not stack:
  print("FRULA")
else:
  print("".join(stack))