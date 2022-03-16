def checkmelody(target, melody):
    for i in range(0, len(melody) - len(target) + 1):
        if(target == melody[i:i +len(target)]):
            if(i+len(target) == len(melody)):
                return True
            if (melody[i+len(target)].isalpha()):
                return True
    return False
def time_to_minute(time):
    hours, minutes = time.split(':')
    return int(hours)*60 + int(minutes)
def solution(m, musicinfos):
    answer = []
    for musicinfo in musicinfos:
        start, end, title, melody = musicinfo.split(',')
        runningtime = time_to_minute(end) - time_to_minute(start)
        fullmelody = ""
        bonus = 0
        for i in range(runningtime):
            j = i + bonus
            fullmelody += melody[j%len(melody)]
            if not(melody[(j+1)%len(melody)].isalpha()):
                fullmelody += melody[(j+1)%len(melody)]
                bonus += 1
        print(fullmelody)
        if(checkmelody(m, fullmelody)):
            answer.append([runningtime, title])
    if(answer):
        answer.sort(key = lambda x : x[0], reverse = True)
        return answer[0][1]
    else:
        return "(None)"