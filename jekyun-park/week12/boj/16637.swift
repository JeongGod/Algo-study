//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/03/19.
//  BOJ > 16637 > 괄호 추가하기

import Foundation

let n = Int(readLine()!)
var formula = (readLine()!).map { Character(extendedGraphemeClusterLiteral: $0) }
var answer = Int.min
var numbers: [Int] = []
var operators: [Character] = []

for char in formula {
    if char.isNumber {
        numbers.append(char.wholeNumberValue!)
    } else {
        operators.append(char)
    }
}
var brackets: [Bool] = Array(repeating: false, count: operators.count)

func selectBracket(_ index: Int) {

    guard index < brackets.count else {
        calculateFormula()
        return
    }

    brackets[index] = true
    selectBracket(index + 2)
    brackets[index] = false
    selectBracket(index + 1)

}


func calculate(_ lhs: Int, _ rhs: Int, _ operation: Character) -> Int {
    switch operation {
    case "+":
        return lhs + rhs
    case "*":
        return lhs * rhs
    case "-":
        return lhs - rhs
    default:
        return 0
    }
}

func calculateFormula() {
    var candidates = numbers

    for index in brackets.indices where brackets[index] {
        candidates[index] = calculate(candidates[index], candidates[index + 1], operators[index])
    }

    for (idx, value) in operators.enumerated() {
        candidates[idx + 1] = brackets[idx] ? candidates[idx] : calculate(candidates[idx], candidates[idx + 1], value)
    }

    if answer < candidates.last! {
        answer = candidates.last!
    }
}


selectBracket(0)

print(answer)



