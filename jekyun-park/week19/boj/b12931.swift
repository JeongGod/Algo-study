//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/05/16.
//  BOJ > 12931 > 두 배 더하기

import Foundation

let N = Int(readLine()!)!

var A = Array(repeating: 0, count: N)
var B = readLine()!.split(separator: " ").map { Int($0)! }

/*
 가능한 연산은 두개 중 하나
 
 배열에 있는 값 하나를 1 증가
 배열에 있는 모든 값을 두배 시킨다
 
 반대로 B->A 로 간다고 하면
 배열에 있는 값 하나를 1 감소
 배열에 있는 모든 값을 2로 나눈다
 를 사용하여 B의 모든 값을 0으로 하여 B를 A로 만들도록 하자
 
 연산의 최소 횟수를 구하여라
 */


var sum = B.reduce(0, +)
var answer = 0

func calculateDivide() {
    for i in 0..<B.count {
        B[i] /= 2
        sum -= B[i]
    }
}

while sum > 0 {
    var isDivisible = true
    for i in 0..<N {
        if B[i] % 2 != 0 {
            isDivisible = false
            B[i] -= 1
            answer += 1
            sum -= 1
        }
    }

    if isDivisible {
        calculateDivide()
        answer += 1
    }
}

print(answer)
