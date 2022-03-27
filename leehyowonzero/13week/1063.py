
def convertpos(pos):
    code = {
        "A" : 1,
        "B" : 2,
        "C" : 3,
        "D" : 4,
        "E" : 5,
        "F" : 6,
        "G" : 7,
        "H" : 8,
    }
    x = int(pos[1])
    y = code[pos[0]]
    return [x, y]


king, stone, n = input().split()
kingpos = convertpos(king)
stonepos = convertpos(stone)
keycode = {
    "R" : [0, 1],
    "L" : [0, -1],
    "B" : [-1, 0],
    "T" : [1, 0],
    "RT" : [1, 1],
    "LT" : [1, -1],
    "RB" : [-1, 1],
    "LB" : [-1, -1],
    
}
code = {
    1 : "A",
    2 : "B",
    3 : "C",
    4 : "D",
    5 : "E",
    6 : "F",
    7 : "G",
    8 : "H",
    }
for _ in range(int(n)):
    command = input()
    movedir = keycode[command]
    nextkingpos = [kingpos[0] + movedir[0], kingpos[1] + movedir[1]]
    if not(1 <= nextkingpos[0] < 9 and 1 <= nextkingpos[1] < 9):
        continue
    if(nextkingpos == stonepos):
        nextstonepos = [stonepos[0] + movedir[0], stonepos[1] + movedir[1]]
        if not(1 <= nextstonepos[0] < 9 and 1 <= nextstonepos[1] < 9):
            continue
        stonepos = nextstonepos
    kingpos = nextkingpos

king =  code[kingpos[1]] + str(kingpos[0])
stone =  code[stonepos[1]] + str(stonepos[0])
print(king)
print(stone)