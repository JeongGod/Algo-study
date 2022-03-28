//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/03/27.
//  BOJ > 2563 > 색종이

import Foundation

let n = Int(readLine()!)!

var map: [[Int]] = Array(repeating: Array(repeating: 0, count: 100), count: 100)
var papers: [[Int]] = []

for _ in 0..<n {
    papers.append(readLine()!.split(separator: " ").map { Int($0)! })
}

for paper in papers {

    for i in paper[0] - 1..<paper[0] + 9 {
        for j in paper[1] - 1..<paper[1] + 9 {
            map[i][j] = 1
        }
    }

}

print(map.flatMap { $0 }.filter { $0 != 0 }.count)






