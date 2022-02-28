//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/02/27.
//  BOJ > 14503 > 로봇 청소기

import Foundation

let inputs = readLine()!.split(separator: " ").map { Int($0)! }
var location = readLine()!.split(separator: " ").map { Int($0)! }
var map: [[Int]] = []
var answer = 0

for _ in 0..<inputs[0] {
    map.append(readLine()!.split(separator: " ").map { Int($0)! })
}

var robot = (r: location[0], c: location[1], direction: location[2])
// d = 0,1,2,3 (북,동,남,서)


// 현재 방향기준으로 돌때
// 서 북 동 남
let dr: [Int] = [0, -1, 0, 1]
let dc: [Int] = [-1, 0, 1, 0]

while true {

    if map[robot.r][robot.c] == 0 {
        map[robot.r][robot.c] = 2
        answer += 1
    }

    if (map[robot.r][robot.c - 1] == 1 || map[robot.r][robot.c - 1] == 2) && (map[robot.r][robot.c + 1] == 1 || map[robot.r][robot.c + 1] == 2) && (map[robot.r - 1][robot.c] == 1 || map[robot.r - 1][robot.c] == 2) && (map[robot.r + 1][robot.c] == 1 || map[robot.r + 1][robot.c] == 2) {
        if robot.direction == 0 {
            robot.r += 1
        } else if robot.direction == 1 {
            robot.c -= 1
        } else if robot.direction == 2 {
            robot.r -= 1
        } else if robot.direction == 3 {
            robot.c += 1
        }
        
        if map[robot.r][robot.c] == 1 { break }
        
        continue
    }
    
    // while true
    for _ in 0..<4 {
        let newRow = robot.r + dr[robot.direction]
        let newColumn = robot.c + dc[robot.direction]

        if map[newRow][newColumn] == 0 {
            robot.r = newRow
            robot.c = newColumn
            robot.direction = (robot.direction - 1) < 0 ? 3 : robot.direction - 1
            break
        } else {
            robot.direction = (robot.direction - 1) < 0 ? 3 : robot.direction - 1
        }
    }
}

print(answer)
