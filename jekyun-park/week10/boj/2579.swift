//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/03/05.
//  BOJ > 2579 > 계단 오르기


/*
 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
 마지막 도착 계단은 반드시 밟아야 한다.
*/

import Foundation

let n = Int(readLine()!)!
var stairs: [Int] = []
var dp = Array(repeating: 0, count: n)

for i in 0..<n {
    stairs.append(Int(readLine()!)!)

    if i == 0 { dp[i] = stairs[i] }
    else if i == 1 { dp[i] = max(dp[0] + stairs[1], stairs[1]) }
    else if i == 2 { dp[i] = max(dp[0] + stairs[2], stairs[1] + stairs[2]) }
    else { dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i]) }

}

print(dp[n-1])



