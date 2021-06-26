from collections import deque


def solution(m, musicinfos):
    m = change(m)
    answer = ('(None)', 0)
    for musicinfo in musicinfos:
        info = musicinfo.split(',')
        time_info = (int(info[1][:2]) - int(info[0][:2])) * 60 + (int(info[1][3:]) - int(info[0][3:]))
        mel = change(info[3])
        played_mel = (mel*time_info)[:time_info]
        if m in played_mel:
            if (time_info > answer[1] or answer[1] == None) :
                answer = (info[2],time_info)
    return answer[0]


def change(melody):
    if 'A#' in melody:
        melody = melody.replace('A#', 'a')
    if 'C#' in melody:
        melody = melody.replace('C#', 'c')
    if 'D#' in melody:
        melody = melody.replace('D#', 'd')
    if 'F#' in melody:
        melody = melody.replace('F#', 'f')
    if 'G#' in melody:
        melody = melody.replace('G#', 'g')
    return melody




print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]	))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("ABC", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:14,WORLD,ABCDEF"]))
print(solution("ABC", ["12:00,14:14,HELLO,CDEFGAB", "13:30,15:14,WORLD,ABCDEF"]))
