//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/03/07.
//  2018 kAKAO BLIND RECRUITMENT > 방금그곡

import Foundation

func solution(_ m: String, _ musicinfos: [String]) -> String {
    // musicinfos: 음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보
    // m: 기억한 멜로디

    let m = m.replacingOccurrences(of: "C#", with: "c").replacingOccurrences(of: "D#", with: "d").replacingOccurrences(of: "F#", with: "f").replacingOccurrences(of: "G#", with: "g").replacingOccurrences(of: "A#", with: "a")
    var resultArray: [(music: String, playTime: Int, name: String)] = []

    for info in musicinfos {
        let information = info.split(separator: ",")
        let name = String(information[2])
        let startTime = information[0].split(separator: ":").map { Int($0)! }[0] * 60 + information[0].split(separator: ":").map { Int($0)! }[1]
        let endTime = information[1].split(separator: ":").map { Int($0)! }[0] * 60 + information[1].split(separator: ":").map { Int($0)! }[1]
        let playTime = endTime - startTime
        var music = String(information[3])

        music = music.replacingOccurrences(of: "C#", with: "c").replacingOccurrences(of: "D#", with: "d").replacingOccurrences(of: "F#", with: "f").replacingOccurrences(of: "G#", with: "g").replacingOccurrences(of: "A#", with: "a")
        
        if music.count > playTime {
            let offset = playTime
            music = String(music[music.startIndex..<music.index(music.startIndex, offsetBy: offset)])

        } else if music.count < playTime {
            let quotient = playTime / music.count
            let remainder = playTime % music.count
            var temp = ""
            for _ in 0..<quotient {
                temp += music
            }
            music = temp + music[music.startIndex..<music.index(music.startIndex, offsetBy: remainder)]
        }

        if music.contains(m) {
            resultArray.append((music, playTime, name))
        }
    }

    return resultArray.max { $0.playTime > $1.playTime }?.name ?? "(None)"
}


//print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
//print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
//print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
