//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/04/01.
//  Programmers > Summer-Winter Coding (2019) > 멀쩡한 사각형

import Foundation

func solution(_ w: Int, _ h: Int) -> Int64 {

    var answer: Int64 = Int64(w*h)
    var a = w
    var b = h

    var r = 0
    
    while b != 0 {
        r = a % b
        a = b
        b = r
    }
    
    let gcd = (a)
    
    answer -= Int64(w+h-gcd)
    
    return answer
}

// print(solution(8, 12))
