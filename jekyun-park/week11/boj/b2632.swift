//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/03/13.
//  BOJ > 2032 > 피자 판매

import Foundation

func makePizzaPieces(_ array: [Int]) -> [Int: Int] {
    
    var dictionary = [Int: Int]()
    
    for i in 0..<array.count {
        var temp = 0
        
        for j in i..<i + array.count - 1 {
            temp += array[j % array.count]
            dictionary[temp, default: 0] += 1
        }
    }
    // reduce
    dictionary[array.reduce(0, +), default: 0] += 1

    return dictionary
}

func binarySearch(_ target: Int) -> Int? {
    var start = 0
    var end = BPieces.count - 1

    while start <= end {
        let mid = (start + end) / 2

        if BPieces[mid] == target {
            return BPieces[mid]
        } else if BPieces[mid] > target {
            end = mid - 1
        } else {
            start = mid + 1
        }
    }
    return nil
}

let targetSize: Int = Int(readLine()!)!
let numberOfPieces = readLine()!.split(separator: " ").map { Int($0)! }
var pizzaA: [Int] = []
var pizzaB: [Int] = []
var answer = 0

for _ in 0..<numberOfPieces[0] {
    pizzaA.append(Int(readLine()!)!)
}

for _ in 0..<numberOfPieces[1] {
    pizzaB.append(Int(readLine()!)!)
}

var ADictionary = makePizzaPieces(pizzaA)
var BDictionary = makePizzaPieces(pizzaB)
ADictionary[0] = 1
BDictionary[0] = 1

let Apieces = [Int](ADictionary.keys).sorted()
let BPieces = [Int](BDictionary.keys).sorted()

for a in Apieces where a <= targetSize {

    guard a != targetSize else {
        answer += ADictionary[a]!
        break
    }
    
    guard let b = binarySearch(targetSize-a) else {
        continue
    }
    
    answer += ADictionary[a]! * BDictionary[b]!

}

print(answer)


