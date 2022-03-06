//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/03/03.
//  Programmers > 탐욕법(Greedy) > 큰 수 만들기

import Foundation

func solution(_ number: String, _ k: Int) -> String {

    var k = k
    var stack: [String] = []

    for num in number {
        
        while !stack.isEmpty && Int(stack.last!)! < Int(exactly: num.wholeNumberValue!)! && k > 0 {
            stack.removeLast()
            k -= 1
        }
        
        stack.append(String(num))
    }
    
    // 남은 k개의 수에 대해
    while k > 0 {
        stack.removeLast()
        k -= 1
    }
    
    return stack.joined()
}


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))





