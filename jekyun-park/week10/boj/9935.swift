//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/03/05.
//  BOJ > 9935 > 문자열 폭발

import Foundation

var inputString = Array(readLine()!).map { String($0) }
let explosionString = readLine()!
let explosionStringArray = Array(explosionString).map { String($0) }
let explosionStringLength = explosionString.count
var stack: [String] = []

for char in inputString {
    stack.append(char)

    if char == explosionStringArray.last! {
        let stackLength = stack.count

        if stackLength >= explosionStringLength && stack[(stackLength - explosionStringLength)...].joined() == explosionString {
            for _ in 0..<explosionStringLength {
                stack.removeLast()
            }
        }
    }
}

let answer = stack.joined()

print(answer.isEmpty ? "FRULA" : answer)


