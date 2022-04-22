//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/04/22.
//  BOJ > 2904 > 수학은 너무 쉬워

import Foundation

let N = Int(readLine()!)!
let paper = readLine()!.split(separator: " ").map { Int($0)! }
let MAX = 1_000_000
var isPrime = Array(repeating: true, count: MAX + 1)
var visited = Array(repeating: 0, count: MAX + 1)

func getNumberOfPrime() {
    for i in 2...MAX {
        if i * i > MAX { break }
        if (!isPrime[i]) { continue }
        for j in stride(from: i * i, through: MAX, by: i) {
            isPrime[j] = false
        }
    }
}

func power(_ x: Int, _ y: Int) -> Int {
    var res = 1; var x = x; var y = y
    while y > 0 {
        if (y % 2) == 1 {
            res = res * x
        }
        y /= 2
        x = x * x
    }
    return res
}

getNumberOfPrime()
var primeArray: [Int] = []
for i in 2...MAX {
    if isPrime[i] {
        primeArray.append(i)
    }
}

var numberOfUsedPrimes = Array(repeating: Array(repeating: 0, count: primeArray.count), count: N)

for i in 0..<paper.count {
    var score = paper[i]
    for j in 0..<primeArray.count {
        if score == 1 { break }
        while (score % primeArray[j] == 0) {
            score /= primeArray[j]
            visited[primeArray[j]] += 1
            numberOfUsedPrimes[i][j] += 1
        }
    }
}

var gcd = 1
var count = 0

for i in 0..<primeArray.count {
    let distribution = visited[primeArray[i]] / N
    for j in 0..<N {
        if numberOfUsedPrimes[j][i] < distribution {
            count += distribution - numberOfUsedPrimes[j][i]
        }
    }
    gcd *= power(primeArray[i], distribution)
}

print(gcd,count)
