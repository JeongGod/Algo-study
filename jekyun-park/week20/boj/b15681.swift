//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/05/20.
//  BOJ > 15681 > 트리와 쿼리

import Foundation

let inputs = readLine()!.split(separator: " ").map { Int($0)! }
let N = inputs[0], R = inputs[1], Q = inputs[2]


func countNodes(_ n: Int) {
    count[n] = 1
    for i in tree[n] {
        if count[i] == 0 {
            countNodes(i)
            count[n] += count[i]
        }
    }
}
var tree = Array(repeating: [Int](), count: N + 1)
var count = Array(repeating: 0, count: N + 1)

for _ in 0..<N - 1 {
    let uv = readLine()!.split(separator: " ").map { Int($0)! }
    let u = uv.first!, v = uv.last!
    tree[u].append(v)
    tree[v].append(u)
}

countNodes(R)

for _ in 0..<Q {
    let query = Int(readLine()!)!
    print(count[query])
}
