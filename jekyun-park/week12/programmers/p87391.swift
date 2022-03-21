//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/03/15.
//  Programmers > 월간 코드 챌린지 시즌3 > 공 이동 시뮬레이션

import Foundation


func solution(_ n: Int, _ m: Int, _ x: Int, _ y: Int, _ queries: [[Int]]) -> Int64 {

    /*
     쿼리를 거꾸로 돌면서 x,y로 도착이 가능한 좌표의 범위를 찾는다.
     */

    var answer: Int64 = 0
    var minPosition = (row: x, column: y)
    var maxPosition = (row: x, column: y)

    for query in queries.reversed() {

        let command = query[0]
        let dx = query[1]

        // 오른쪽으로
        if command == 0 {

            if minPosition.column != 0 { minPosition.column = minPosition.column + dx }
            maxPosition.column = maxPosition.column + dx < m - 1 ? maxPosition.column + dx : m - 1
            if m < minPosition.column { return 0 }

            // 왼쪽으로
        } else if command == 1 {

            minPosition.column = 0 < minPosition.column - dx ? minPosition.column - dx: 0
            if maxPosition.column != m - 1 { maxPosition.column = maxPosition.column - dx }
            if maxPosition.column < 0 { return 0 }

            // 아래로
        } else if command == 2 {

            if minPosition.row != 0 { minPosition.row = minPosition.row + dx }
            maxPosition.row = maxPosition.row + dx < n - 1 ? maxPosition.row + dx : n - 1
            if n < minPosition.row { return 0 }

            // 위로
        } else {

            minPosition.row = 0 < minPosition.row - dx ? minPosition.row - dx: 0
            if maxPosition.row != n - 1 { maxPosition.row = maxPosition.row - dx }
            if maxPosition.row < 0 { return 0 }

        }
    }

    answer = Int64((maxPosition.row - minPosition.row + 1) * (maxPosition.column - minPosition.column + 1))

    return answer
}


print(solution(2, 2, 0, 0, [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]]))
print(solution(2, 5, 0, 1, [[3, 1], [2, 2], [1, 1], [2, 3], [0, 1], [2, 1]]))
//print(solution(10, 3, 0, 0, [[2, 3], [1, 0], [3, 32], [0, 14]]))
