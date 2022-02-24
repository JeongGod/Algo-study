//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/02/21.
//  BOJ > 19236 > 청소년 상어

import Foundation

struct Fish {
    var isLive: Bool
    var num: Int
    var direction: Int
    var row: Int
    var column: Int
    init(_ isLive: Bool, _ num: Int, _ dir: Int, _ row: Int, _ column: Int) {
        self.isLive = isLive
        self.num = num
        self.direction = dir
        self.row = row
        self.column = column

    }
}

var fishes: [Fish] = Array(repeating: Fish.init(true, 0, 0, 0, 0), count: 17)
var space: [[Int]] = Array(repeating: Array(repeating: 0, count: 4), count: 4)
let direction: [Int: (Int, Int)] = [1: (-1, 0), 2: (-1, -1), 3: (0, -1), 4: (1, -1), 5: (1, 0), 6: (1, 1), 7: (0, 1), 8: (-1, 1)]
var score = 0

for i in 0..<4 {
    let input = readLine()!.split(separator: " ").map { Int($0)! }

    for j in 0..<4 {
        space[i][j] = input[2 * j]
        let num = input[2 * j]
        let dir = input[2 * j + 1]
        fishes[num] = Fish(true, num, dir, i, j)
    }
}
//fishes.sort { $0.num < $1.num }


func dfs(_ map: [[Int]], _ fishArray: [Fish], _ sharkRow: Int, _ sharkColumn: Int, _ sharkScore: Int) {

    var copiedMap = map
    var copiedFishes = fishArray

    let fishNum = copiedMap[sharkRow][sharkColumn]
    let sharkDirection = copiedFishes[fishNum].direction
    copiedFishes[fishNum].isLive = false
    copiedMap[sharkRow][sharkColumn] = -1

    var newSharkScore = sharkScore
    newSharkScore += fishNum
    if score < newSharkScore { score = newSharkScore }

    for i in 1...16 {
        if copiedFishes[i].isLive == false { continue }

        let currentRow = copiedFishes[i].row
        let currentColumn = copiedFishes[i].column
        let currentDirection = copiedFishes[i].direction

        var newRow = currentRow + direction[currentDirection]!.0
        var newColumn = currentColumn + direction[currentDirection]!.1
        var newDirection = currentDirection

        while (newRow < 0 || newColumn < 0 || newRow >= 4 || newColumn >= 4 || (newRow == sharkRow && newColumn == sharkColumn)) {
            newDirection = (newDirection) % 8 + 1
            newRow = currentRow + direction[newDirection]!.0
            newColumn = currentColumn + direction[newDirection]!.1
        }
        
        if copiedMap[newRow][newColumn] != -1 {

            let targetFishNumber = copiedMap[newRow][newColumn]

            copiedFishes[targetFishNumber].row = currentRow
            copiedFishes[targetFishNumber].column = currentColumn

            copiedFishes[i].row = newRow
            copiedFishes[i].column = newColumn
            copiedFishes[i].direction = newDirection

            copiedMap[newRow][newColumn] = i
            copiedMap[currentRow][currentColumn] = targetFishNumber

        } else {
            copiedFishes[i].row = newRow
            copiedFishes[i].column = newColumn
            copiedFishes[i].direction = newDirection

            copiedMap[newRow][newColumn] = i
            copiedMap[currentRow][currentColumn] = -1
        }
    }

    for i in 1...3 {
        let newRow = sharkRow + direction[sharkDirection]!.0 * i
        let newColumn = sharkColumn + direction[sharkDirection]!.1 * i

        if (newRow < 0 || newColumn < 0 || newRow >= 4 || newColumn >= 4) { break }
        
        if copiedMap[newRow][newColumn] != -1 {
            dfs(copiedMap, copiedFishes, newRow, newColumn, newSharkScore)
        }
    }
}

dfs(space, fishes, 0, 0, 0)

print(score)
