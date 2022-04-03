//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/04/01.
//  Programmers > 2017 팁스다운 > 예상 대진표

import Foundation

func solution(_ n: Int, _ a: Int, _ b: Int) -> Int {

    var round = 0
    var a = a
    var b = b

    while a != b {

        if a % 2 != 0 {
            a += 1
        }
        a /= 2

        if b % 2 != 0 {
            b += 1
        }
        b /= 2

        round += 1
    }

    return round
}

//print(solution(8, 4, 7))
