//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/01/12.
//

import Foundation

func solution(_ places:[[String]]) -> [Int] {
    
    var answerArray: [Int] = []
    
    for testSite in places { // ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]
        
        // P 위치 저장
        var personLocations: [(Int,Int)] = []
        
        // 인덱스로 접근하여 좌표를 알아내기 위하여 문자열을 쪼갬
        // p => [["P", "O", "O", "O", "P"], ["O", "X", "X", "O", "X"], ["O", "P", "X", "P", "X"], ["O", "O", "X", "O", "X"], ["P", "O", "X", "X", "P"]]
        let p = testSite.map{ $0.map{ String($0) } }
        
        
        for i in 0..<5 {
            for j in 0..<5 {
                if isPerson(p, i, j) {
                    personLocations.append((i,j))
                }
                
            }
        }
        
        // 1 : 거리두기O, 0 : 거리두기 X
        var isDistanced = 1
        
        if !personLocations.isEmpty { // person의 모든 쌍을 따져봄
            for i in 0..<personLocations.count-1 {
                for j in i+1..<personLocations.count {
                    if calculateManhattanDistance(personLocations[i], personLocations[j]) == 2 { // 맨해튼 거리 2인 경우
                        if !isPartitionExistBetweenPerson(p, personLocations[i], personLocations[j]) { // 파티션이 사이에 있는지 확인, 파티션 없으면 0 리턴
                            isDistanced = 0
                            break
                        }
                        
                    } else if calculateManhattanDistance(personLocations[i], personLocations[j]) == 1 { // 맨해튼 거리 1인 경우 -> 무조건 0 리턴
                        isDistanced = 0
                        break
                    }
                }
            }
        }
        answerArray.append(isDistanced)
    }
    return answerArray
}


func calculateManhattanDistance(_ a:(Int,Int), _ b:(Int,Int)) -> Int {
    
    var distance: Int = 0
    distance = abs(a.0-b.0) + abs(a.1-b.1)
    
    return distance
}

// 사람인지 아닌지 체크
func isPerson(_ array:[[String]], _ row:Int, _ col:Int) -> Bool {
    return array[row][col] == "P"
}

// 사람 사이에 파티션이 있는가? <-- 여기가 좀 어려움
func isPartitionExistBetweenPerson(_ array: [[String]], _ a: (Int,Int) , _ b: (Int,Int)) -> Bool {
    if a.0 == b.0 { // 가로선상에 놓인 경우
        for i in a.1+1 ..< b.1 {
            if array[a.0][i] != "X" {
                return false
            }
        }
    } else if a.1 == b.1 { // 세로선상에 놓인 경우
        for j in a.0+1 ..< b.0 {
            if array[j][a.1] != "X" {
                return false
            }
        }
    } else { // 대각인경우
        if array[a.0][b.1] != "X" || array[b.0][a.1] != "X" {
            return false
        }
    }
    
    return true
}

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
