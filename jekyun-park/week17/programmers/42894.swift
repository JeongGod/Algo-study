//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/04/21.
//  Programmers > 2019 KAKAO BLIND RECRUITMENT > 블록 게임

import Foundation

func checkPossibility(_ x: Int, _ y: Int, _ board: [[Int]]) -> Bool {
    for i in 0..<x {
        if board[i][y] != 0 { return false }
    }
    return true
}

func findRectangle(_ x: Int, _ y: Int, _ h: Int, _ w: Int, _ board: inout [[Int]]) -> Bool {
    var emptySpace = 0
    var lastBlockNumber = -1

    for i in x..<x + h {
        for j in y..<y + w {
            if board[i][j] == 0 {
                if !checkPossibility(i, j, board) { return false }
                emptySpace += 1
                if emptySpace > 2 { return false }
            } else {
                if (lastBlockNumber != -1 && lastBlockNumber != board[i][j]) {
                    return false
                }
                lastBlockNumber = board[i][j]
            }
        }
    }

    for i in x..<x + h {
        for j in y..<y + w {
            board[i][j] = 0
        }
    }

    return true
}


func solution(_ board: [[Int]]) -> Int {
    var answer = 0
    var newBoard = board
    let N = board.count

    var count: Int
    repeat {
        count = 0
        for i in 0..<N {
            for j in 0..<N {
                if (i <= N - 2 && j <= N - 3 && findRectangle(i, j, 2, 3, &newBoard)) {
                    count += 1
                } else if (i <= N - 3 && j <= N - 2 && findRectangle(i, j, 3, 2, &newBoard)) {
                    count += 1
                }
            }
        }
        answer += count
    } while (count != 0)
    return answer
}


//print(solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0], [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5], [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]))
