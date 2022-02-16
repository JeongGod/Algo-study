//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/02/16.
// 2019 카카오 개발자 겨울 인턴십 > 크레인 인형뽑기 게임 > 64061

import Foundation

func solution(_ board: [[Int]], _ moves: [Int]) -> Int {

    var newBoard = board
    var stack: [Int] = []
    var answer: Int = 0

    for move in moves {

        let location: Int = move-1

        for i in (0..<newBoard.count) {
            if newBoard[i][location] != 0 {
                if stack.last == newBoard[i][location] {
                    stack.popLast()
                    answer += 2
                } else {
                    stack.append(newBoard[i][location])
                }
                newBoard[i][location] = 0
                break
            }
        }
    }
    return answer
}

print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))
