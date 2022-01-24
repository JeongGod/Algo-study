//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/01/23.
//

import Foundation

func solution(_ expression: String) -> Int64 {
    
    let numbers = expression.components(separatedBy: ["*","+","-"]).map { Int64($0)! }
    let operators = Array((expression.filter { !$0.isNumber }))
    
    let setOperators = Array(Set(operators))
    
    let permutations = permutation(setOperators, setOperators.count)

    var answer : Int64 = 0

    for arr in permutations { // 각 조합을 돌면서 계산
        var currentNumbers = numbers, currentOperators = operators
        for op in arr { // 연산자 마다
            while currentOperators.contains(op) {
                if let index = currentOperators.firstIndex(of: op) {
                    switch op {
                    case "*":
                        currentNumbers[index] *= currentNumbers[index + 1]
                    case "+":
                        currentNumbers[index] += currentNumbers[index + 1]
                    case "-":
                        currentNumbers[index] -= currentNumbers[index + 1]
                    default:
                        break
                    }
                    currentNumbers.remove(at: index + 1)
                    currentOperators.remove(at: index)
                }
            }
        }
        answer = max(answer, abs((currentNumbers[0])))
    }
    return answer
}

func permutation<T>(_ elements: [T], _ k: Int) -> [[T]] {
    var result = [[T]]()
    var visited = [Bool](repeating: false, count: elements.count)

    func permut(_ now: [T]) {
        if now.count == k {
            result.append(now)
            return
        }

        for i in 0..<elements.count {
            if visited[i] == true { continue }
            visited[i] = true
            permut(now + [elements[i]])
            visited[i] = false
        }
    }
    permut([])
    return result
}
