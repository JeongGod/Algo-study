//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/03/20.
//  BOJ > 2011 > 암호코드


import Foundation

let password = readLine()!.map { Int(String($0)) }
let modular = 1000000
let n = password.count

var dp = Array(repeating: 0, count: n+1)

dp[0] = 1
dp[1] = 1

if password[0] == 0 {
    print(0)
    exit(1)
} else {
    for i in 2..<n+1 {
        
        if 1 <= password[i-1]! && password[i-1]! <= 9 {
            dp[i] += dp[i-1]
        }
        
        let number = password[i-2]! * 10 + password[i-1]!
        
        if 10 <= number && number <= 26 {
            dp[i] += dp[i-2]
        }
        
        dp[i] %= modular
        
    }
    print(dp[n])
}
