//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/04/10.
//  BOJ > 17073 > 나무 위의 빗물

import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let N = input[0], W = input[1]
var vertexes: [Int: Int] = [:]
var numberOfLeafNodes = 0

for _ in 0..<N-1 {
    let uv = readLine()!.split(separator: " ").map { Int($0)! }
    let u = uv[0], v = uv[1]

    vertexes[u, default: 0] += 1
    vertexes[v, default: 0] += 1
}

// 리프 노드의 수
for i in 2...N {
    if vertexes[i] == 1 {
        numberOfLeafNodes += 1
    }
}

print(Double(W)/Double(numberOfLeafNodes))
