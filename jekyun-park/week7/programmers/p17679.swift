//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/02/13.
//

import Foundation

// 판의 높이 m, 폭 n (한 라인의 블록 수)
func solution(_ m: Int, _ n: Int, _ board: [String]) -> Int {

    var newBoard: [[String]] = []
    var answer: Int = 0

    for line in board {
        newBoard.append(Array(line).map { String($0) })
    }
    while true {
        let deleteBlocks = findFourBlock(&newBoard)
        if deleteBlocks.isEmpty { break }
        else {
            answer += deleteBlocks.count
            for block in deleteBlocks {
                newBoard[block[0]][block[1]] = "!"
            }
            fallBoard(&newBoard)
        }
    }
    return answer
}

func fallBoard(_ board: inout [[String]]) -> [[String]] {

    let M = board.count
    let N = board[0].count

    for j in 0..<N {
        var stack: [String] = []
        for i in 0..<M {
            if board[i][j] == "!" { continue }
            stack.append(board[i][j])
            board[i][j] = "!"
        }
        var height = M - 1
        while !stack.isEmpty {
            board[height][j] = stack.popLast()!
            height -= 1
        }
    }

    return board
}

func findFourBlock(_ board: inout [[String]]) -> Set<[Int]> {

    var blocks: Set<[Int]> = []

    for i in 0..<board.count {
        for j in 0..<board[i].count {
            if i == board.count - 1 || j == board[0].count - 1 { continue }
            if board[i][j] == board[i][j + 1] && board[i][j] == board[i + 1][j + 1] && board[i][j] == board[i + 1][j] && board[i][j] != "!" {
                blocks.update(with: [i, j])
                blocks.update(with: [i + 1, j])
                blocks.update(with: [i, j + 1])
                blocks.update(with: [i + 1, j + 1])
            }
        }
    }
    return blocks
}


//print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
