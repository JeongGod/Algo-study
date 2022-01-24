//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/01/22.
//

import Foundation

func solution(_ N: Int, _ stages: [Int]) -> [Int] {

    var failRate: [Int: Double] = [:]
    let numOfPlayers: Double = Double(stages.count)
    var reachedPlayers: [Double] = Array(repeating: 0, count: N+2)
    var notClearedPlayers: Double = 0
    
    for stage in stages {
        reachedPlayers[stage] += 1
    }
    

    for i in 1...N {
        if reachedPlayers[i] == 0 {
            failRate[i] = 0
            continue
        }
        
        failRate[i] = reachedPlayers[i] / (numOfPlayers-notClearedPlayers)
        notClearedPlayers += reachedPlayers[i]
    }

    return failRate.sorted(by: <).sorted { $0.value > $1.value }.map({ $0.key })
}

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))


import Foundation

func solution2(_ N:Int, _ stages:[Int]) -> [Int] {

    var failure: [Int: Float] = [:]
    var player: Int = stages.count

    for i in 1...N {
        let n = stages.lazy.filter { $0 == i }.count
        failure[i] = Float(n)/Float(player)
        player -= n
    }

    return failure.lazy.sorted(by: <).sorted(by: { $0.value > $1.value }).map {$0.key}
}
