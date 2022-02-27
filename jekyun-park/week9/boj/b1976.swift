//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/02/24.
//  BOJ > 1976번 : 여행가자

import Foundation

let N = Int(readLine()!)!
let M = Int(readLine()!)!

var moveDictionary: [Int: [Int]] = [:]

for i in 0..<N {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    for j in 0..<input.count {
        if input[j] == 1 {
            if moveDictionary[i] != nil {
                moveDictionary[i]?.append(j)
            } else {
                moveDictionary[i] = [j]
            }
        }
    }
}

var plan = readLine()!.split(separator: " ").map { Int($0)! - 1 }
var planSet: Set<Int> = Set(plan)

var stack: [Int] = []
var visited: Set<Int> = []

stack.append(plan[0])
visited.update(with: plan[0])

while !stack.isEmpty {
    let currentCity = stack.popLast()!

    if moveDictionary[currentCity] != nil {
        for city in moveDictionary[currentCity]! {
            if visited.contains(city) { continue }
            stack.append(city)
            visited.update(with: city)
        }
    }

}

if visited.isSuperset(of: planSet) {
    print("YES")
} else {
    print("NO")
}
