//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/05/17.
//  BOJ > 7682 > 틱택토

import Foundation

func checkBingo(_ map: [[String]], _ mark: String) -> Bool {
    if map[0][0] == map[0][1] && map[0][1] == map[0][2] && map[0][2] == mark {
        return true
    }
    if map[1][0] == map[1][1] && map[1][1] == map[1][2] && map[1][2] == mark {
        return true
    }
    if map[2][0] == map[2][1] && map[2][1] == map[2][2] && map[2][2] == mark {
        return true
    }
    if map[0][0] == map[1][0] && map[1][0] == map[2][0] && map[2][0] == mark {
        return true
    }
    if map[0][1] == map[1][1] && map[1][1] == map[2][1] && map[2][1] == mark {
        return true
    }
    if map[0][2] == map[1][2] && map[1][2] == map[2][2] && map[2][2] == mark {
        return true
    }
    if map[0][0] == map[1][1] && map[1][1] == map[2][2] && map[2][2] == mark {
        return true
    }
    if map[0][2] == map[1][1] && map[1][1] == map[2][0] && map[2][0] == mark {
        return true
    }
    return false
}


var totalMap: [[String]] = []

while true {
    let input = readLine()!.map { String($0) }
    if input == ["e", "n", "d"] {
        break
    }
    totalMap.append(input)
}

for i in 0..<totalMap.count {

    let game = totalMap[i]
    var board = Array(repeating: Array(repeating: "", count: 3), count: 3)

    var count = 0
    var oCount = 0
    var xCount = 0
    var blankCount = 0

    for i in 0..<3 {
        for j in 0..<3 {
            board[i][j] = game[count]
            count += 1
            if board[i][j] == "O" {
                oCount += 1
            } else if board[i][j] == "X" {
                xCount += 1
            } else {
                blankCount += 1
            }
        }
    }

    if xCount > oCount + 1 {
        print("invalid")
        continue
    }

    if oCount > xCount {
        print("invalid")
        continue
    }

    if oCount == xCount {
        if checkBingo(board, "O") && !checkBingo(board, "X") {
            print("valid")
            continue
        }
    }

    if oCount + 1 == xCount {
        if checkBingo(board, "X") && !checkBingo(board, "O") {
            print("valid")
            continue
        }
    }

    if xCount == 5 && oCount == 4 {
        if !checkBingo(board, "O") {
            print("valid")
            continue
        }
    }
    
    print("invalid")
}

