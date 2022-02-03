//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/01/31.
//

import Foundation

// (도시에있는) g 금무게 s 은무게 t 편도이동시간 w 최대운반무게
// a 필요한 금의양, b 필요한 은의양
func solution(_ a: Int, _ b: Int, _ g: [Int], _ s: [Int], _ w: [Int], _ t: [Int]) -> Int64 {

    var start: Int = 0
    var end: Int = Int(10e15)
    var answer: Int = end

    while start <= end {
        // mid 는 이동시간을 나타냄
        let mid = (start + end) / 2
        var gold = 0
        var silver = 0
        var total = 0

        for i in 0..<s.count {
            // count: 이동시간 내에 운반할 수 있는 횟수
            var count = mid / (t[i] * 2)

            if mid % (t[i] * 2) >= t[i] {
                count += 1
            }
            
            // 시간내에 운반가능한 무게와 각 트럭의 금,은의 무게를 비교
            gold += min(g[i], w[i] * count)
            silver += min(s[i], w[i] * count)
            total += min(g[i] + s[i], w[i] * count)
        }
        
        // 위에서 구한 모든 트럭의 광물의 합의 최대치가 조건을 만족하는지 검사
        // a,b : 필요한 금,은의 양
        // a
        if gold >= a && silver >= b && total >= a + b {
            end = mid - 1
            answer = min(mid, answer)
        } else {
            start = mid + 1
        }
        
    }
    return Int64(answer)
}

print(solution(10, 10, [100], [100], [7], [10]))
print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))
// 10    10    [100]    [100]    [7]    [10]
// 90    500    [70,70,0]    [0,0,500]    [100,100,2]    [4,8,1]
