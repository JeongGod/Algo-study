//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/01/22.
// programmers > Summer/Winter Coding(~2018) 방문길이

// 캐릭터가 처음 걸어본 길의 길이를 구하라

import Foundation

func solution(_ dirs: String) -> Int {
    
    // 시작 위치
    var coord = (0, 0)
    var set = Set<String>()

    for dir in dirs {
        
        // 현재 좌표
        var point = coord
        var x = point.0
        var y = point.1
        
        // 계산
        if dir == "U" {
            y += 1
        } else if dir == "D" {
            y -= 1
        } else if dir == "L" {
            x -= 1
        } else if dir == "R" {
            x += 1
        }
        
        // 범위 체크
        if x > 5 || x < -5 {
            continue
        }

        if y > 5 || y < -5 {
            continue
        }
        
        point.0 = x
        point.1 = y
        
        // 중복 확인, 이동한좌표,현재좌표가 set에 없으면 현재좌표,이동한좌표를 set에 insert
        if !set.contains("\(point)\(coord)") {
            set.insert("\(coord)\(point)")
        }
        
        // 갱신
        coord = point

    }

    return set.count
}


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
