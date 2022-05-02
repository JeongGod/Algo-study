//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/05/02.
//  BOJ > 10775 > 공항

import Foundation

let G = Int(readLine()!)!
let P = Int(readLine()!)!
var gates = [Int]()
var parent = Array(0...G)

func find(_ n: Int) -> Int {
    if n == parent[n] { return n }
    return find(parent[n])
}

func union(_ a: Int, _ b: Int) {
    parent[a] = parent[b]
}

var answer = 0

for _ in 0..<P {
    gates.append(Int(readLine()!)!)
}

for i in gates {
    let parent = find(i)
    if parent == 0 { break }
    answer += 1
    union(parent, parent-1)
}

print(answer)
