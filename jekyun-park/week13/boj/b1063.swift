//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/03/27.
//  BOJ > 1063 > 킹

import Foundation

let input = readLine()!.split(separator: " ")
let N = Int(input[2])!

let alphabetsToColumn: [String: Int] = ["A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8]
let columnToAlphabets: [Int: String] = [1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H"]
let vectors: [String: (Int, Int)] = ["R": (1, 0), "L": (-1, 0), "B": (0, -1), "T": (0, 1), "RT": (1, 1), "LT": (-1, 1), "RB": (1, -1), "LB": (-1, -1)]

var kingLocation = input[0].map { String($0) }
var king: (Int, Int) = (alphabetsToColumn[kingLocation[0]]!, Int(kingLocation[1])!)
var stoneLocation = input[1].map { String($0) }
var stone: (Int, Int) = (alphabetsToColumn[stoneLocation[0]]!, Int(stoneLocation[1])!)

for _ in 0..<N {

    let move = readLine()!

    let nx = king.0 + vectors[move]!.0
    let ny = king.1 + vectors[move]!.1

    if nx < 1 || nx > 8 || ny < 1 || ny > 8 {
        continue
    }

    if (nx, ny) == stone {

        if stone.0 + vectors[move]!.0 < 1 || stone.1 + vectors[move]!.1 > 8 || stone.1 + vectors[move]!.1 < 1 || stone.0 + vectors[move]!.0 > 8 {
            continue
        }
        
        king = (nx, ny)
        stone = (stone.0 + vectors[move]!.0, stone.1 + vectors[move]!.1)

    } else {

        king = (nx, ny)
    }


}

let kingString = columnToAlphabets[king.0]! + "\(king.1)"
let stoneString = columnToAlphabets[stone.0]! + "\(stone.1)"

print(kingString)
print(stoneString)
