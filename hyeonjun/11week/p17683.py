sharp = {'A#': 'a', 'C#': 'c', 'D#': 'd', 'E#': 'e', 'F#': 'f', 'G#': 'g'}


def solution(m, musicinfos):
    answer = ['(None)', 0]

    def get_time(start, end):
        h = int(end[:2]) - int(start[:2])
        m = int(end[3:]) - int(start[3:])
        return h * 60 + m

    def split_melody(target):
        res = ''
        for note in target:
            if note == '#':
                res = res[:-1] + sharp[res[-1]+note]
            else:
                res += note
        return res

    m = split_melody(m)
    for musicinfo in musicinfos:
        start, end, title, melody = musicinfo.split(',')
        play_time = get_time(start, end)
        melody = split_melody(melody)
        melody = melody*(play_time//len(melody)) + \
            melody[:play_time % len(melody)]

        if m in melody and answer[1] < play_time:
            answer = [title, play_time]

    return answer[0]
