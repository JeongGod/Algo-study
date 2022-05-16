//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/05/15.
//  BOJ > 1107 > 리모컨

import Foundation

var isBroke = Array(repeating: false, count: 10)

let N = Int(readLine()!)!

let M = Int(readLine()!)!

if M != 0 {
    readLine()!.split(separator: " ").map { Int($0)! }.forEach { isBroke[$0] = true }
}

var minimum = abs(100 - N)

for number in 0..<1000001 {
    var stringNumber = String(number)

    for (index, value) in stringNumber.enumerated() {
        if isBroke[(value).wholeNumberValue!] {
            break
        } else if index == stringNumber.count - 1 {
            minimum = min(minimum, abs(Int(stringNumber)!-N)+stringNumber.count)
        }
    }
}

print(minimum)
