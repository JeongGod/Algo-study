//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/04/30.
//  BOJ > 16938 > 캠프 준비

import Foundation

func combination<T: Comparable>(_ array: [T], _ n: Int) -> [[T]] {
    var result = [[T]]()
    if array.count < n { return result }

    var stack = array.enumerated().map { ([$0.element], $0.offset) }

    while stack.count > 0 {
        let now = stack.removeLast()

        let elements = now.0
        let index = now.1

        if elements.count == n {
            result.append(elements.sorted())
            continue
        }

        guard index+1 <= array.count-1 else { continue }

        for i in index+1...array.count-1 {
            stack.append((elements + [array[i]], i))
        }
    }

    return result
}

let NLRX = readLine()!.split(separator: " ").map { Int($0)! }
let N = NLRX[0], L = NLRX[1], R = NLRX[2], X = NLRX[3]
let problems = readLine()!.split(separator: " ").map { Int($0)! }
var difficulty = 0
var difference = 0
var answer = 0

for i in 2...N {
    let cases = combination(problems, i)

    for senario in cases {
        difficulty = senario.reduce(0,+)
        difference = senario.max()! - senario.min()!
        if difficulty < L || difficulty > R { continue }
        if difference < X { continue }
        answer += 1
    }
    
}

print(answer)
