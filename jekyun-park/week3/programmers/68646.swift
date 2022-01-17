//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/01/16.
//

import Foundation

/*
 
 [-16,27,65,-2,58,-92,-71,-68,-61,-33]
 
 */

func solution(_ a:[Int]) -> Int {
    
    var answer: Int = 2
    var leftMin = a[0]
    
    // a 배열의 갯수가 3보다 작다면, 2가 답이 된다.
    if a.count < 3 { return 2 }
    
    // i 번째 풍선을 기준으로 해당 풍선 오른쪽 풍선들 중 최솟값을 배열에 저장
    // minimumValues[i] => i번째 풍선의 오른쪽에 있는 풍선들 중 최솟값
    var minimumValues: [Int] = Array(repeating: a.last!, count: a.count-1)
    
    // 거꾸로 for문 실행하여, 배열을 채움
    for i in (1..<a.count-2).reversed() {
        minimumValues[i] = [a[i+1],minimumValues[i+1]].min()!
    }
    
    let isThisBalloonCanSurvive: (Int) -> Bool = { i in
        if a[i] < leftMin {
            leftMin = [leftMin,a[i]].min()!
            return true
        }
        if a[i] < minimumValues[i] {
            return true
        }
        
        return false
    }
    
    for i in 1..<a.count-1 {
        if isThisBalloonCanSurvive(i) { answer += 1 }
    }
    
    return answer
}

// 6
// print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))





