//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/03/21.
//  Programmers > 월간 코드 챌린지 시즌 1 > 삼각 달팽이 (68645)

import Foundation

func solution(_ n: Int) -> [Int] {

    // 내려가기, 오른쪽으로 이동, 올라가기 ( 달팽이 모양으로 진행 )

    let dx = [1, 0, -1]
    let dy = [0, 1, -1]

    var dir = 0
    var row = 0, col = 0
    var number = 1

    var array: [[Int]] = []

    for i in 1...n {
        array.append(Array(repeating: 0, count: i))
    }

    // n-1,n-2,n-3,...,1
    
    for i in (1...n).reversed() {
        for _ in 0..<i - 1 {

            array[row][col] = number
            row += dx[dir]
            col += dy[dir]
            number += 1
        }
        array[row][col] = number
        number += 1
        dir = (dir + 1) % 3
        row += dx[dir]
        col += dy[dir]
    }

    return array.flatMap { $0 }
}

//solution(4)

