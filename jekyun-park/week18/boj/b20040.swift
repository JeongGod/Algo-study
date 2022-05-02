//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/05/01.
//  BOJ > 20040 > 사이클 게임

import Foundation

let NM = readLine()!.split(separator: " ").map { Int($0)! }

//var graph: [Int:[Int]] = [:]
var parent = Array(0...NM[0]-1)
//var visited = Array(repeating: false, count: NM[0])

func union(_ x:Int, _ y:Int) {
    let parentX = findParent(x)
    let parentY = findParent(y)
    if parentX < parentY { parent[parentY] = parentX }
    else { parent[parentX] = parentY }
}

func findParent(_ x:Int ) -> Int {
    if parent[x] == x { return x }
    return findParent(parent[x])
}

for i in 1...NM[1] {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    let a = input[0], b = input[1]
    
    if findParent(a) == findParent(b) {
        print(i)
        exit(0)
    }
    union(a, b)
}

print(0)


