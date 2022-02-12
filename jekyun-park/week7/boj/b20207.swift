//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/02/12.
//

import Foundation

let N = Int(readLine()!)!

var calender = Array(repeating: 0, count: 366)

for _ in 0..<N {
    let schedule = readLine()!.split(separator: " ").map { Int($0)! }
    
    for i in schedule[0]...schedule[1] {
        calender[i] += 1
    }
}

var row = 0
var column = 0
var answer = 0

for i in 0..<366 {
    if calender[i] != 0 {
        row = max(row, calender[i]) // 세로
        column += 1 // 가로
    } else {
        answer += row * column
        row = 0
        column = 0
    }
}
answer += row*column

print(answer)
