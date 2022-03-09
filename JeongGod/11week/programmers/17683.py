def hour_to_min(t):
    hour, minute = map(int, t.split(":"))
    return hour * 60 + minute

def change_music(m):
    change = {
        "C#" : "0",
        "D#" : "1",
        "F#" : "2",
        "G#" : "3",
        "A#" : "4",
    }
    for key in change:
        m = m.replace(key, change[key])
    return m

import re


def solution(m, musicinfos):
    """
    1분에 1개씩 재생된다.
    시간이 음악 길이보다 크면 처음부터 반복재생
    짧다면 재생 시간만큼만 재생
    
    재생된 시간이 제일 길고, 먼저 입력된 음악 제목
    """
    answer = []
    # "C#" => 하나의 숫자로 변환
    m = change_music(m)
    for start, end, title, music in map(lambda x: x.split(","), musicinfos):
        play_time = hour_to_min(end) - hour_to_min(start)
        if play_time < 0:
            play_time = hour_to_min("23:59") - hour_to_min(start)

        # "C#" => 하나의 숫자로 변환
        music = change_music(music)
        cnt, nam = divmod(play_time, len(music))
        all_music = music * cnt + music[:nam]
        
        # pattern을 찾았다면
        pattern = re.compile(m)
        if pattern.search(all_music):
            answer.append((play_time, title))
            
    return sorted(answer, key=lambda x:x[0], reverse=True)[0][1] if answer else "(None)"
