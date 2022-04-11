//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/04/10.
//  BOJ > 15961 > 회전 초밥

import Foundation

final class FileIO {
    private let buffer:[UInt8]
    private var index: Int = 0

    init(fileHandle: FileHandle = FileHandle.standardInput) {
        
        buffer = Array(try! fileHandle.readToEnd()!)+[UInt8(0)] // 인덱스 범위 넘어가는 것 방지
    }

    @inline(__always) private func read() -> UInt8 {
        defer { index += 1 }

        return buffer[index]
    }

    @inline(__always) func readInt() -> Int {
        var sum = 0
        var now = read()
        var isPositive = true

        while now == 10
                || now == 32 { now = read() } // 공백과 줄바꿈 무시
        if now == 45 { isPositive.toggle(); now = read() } // 음수 처리
        while now >= 48, now <= 57 {
            sum = sum * 10 + Int(now-48)
            now = read()
        }

        return sum * (isPositive ? 1:-1)
    }

    @inline(__always) func readString() -> String {
        var now = read()

        while now == 10 || now == 32 { now = read() } // 공백과 줄바꿈 무시
        let beginIndex = index-1

        while now != 10,
              now != 32,
              now != 0 { now = read() }

        return String(bytes: Array(buffer[beginIndex..<(index-1)]), encoding: .ascii)!
    }

    @inline(__always) func readByteSequenceWithoutSpaceAndLineFeed() -> [UInt8] {
        var now = read()

        while now == 10 || now == 32 { now = read() } // 공백과 줄바꿈 무시
        let beginIndex = index-1

        while now != 10,
              now != 32,
              now != 0 { now = read() }

        return Array(buffer[beginIndex..<(index-1)])
    }
}

let file = FileIO()
let (N,d,k,c) = (file.readInt(),file.readInt(),file.readInt(),file.readInt())
var sushi: [Int] = []
for _ in 0..<N {
    sushi.append(file.readInt())
}

var menu = Array(repeating: 0, count: d+1)
var kindSet = Set<Int>()
for i in 0..<k {
    kindSet.insert(sushi[i])
    menu[sushi[i]] += 1
}
var maxKinds = kindSet.contains(c) ? kindSet.count : kindSet.count + 1
for i in k..<sushi.count+k {
    let removeDish = sushi[i-k]
    
    menu[removeDish] -= 1
    if menu[removeDish] == 0 {
        kindSet.remove(removeDish)
    }
    
    let addDish = sushi[i%sushi.count]
    menu[addDish] += 1
    kindSet.insert(addDish)
    
    let kinds = kindSet.contains(c) ? kindSet.count : kindSet.count + 1
    maxKinds = max(kinds,maxKinds)
}

print(maxKinds)
