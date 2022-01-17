//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/01/14.
//

import Foundation


func solution(_ user_id:[String], _ banned_id:[String]) -> Int {
    
    let banIdIndex = findingBanId(user_id, banned_id)
    
    var answerSet = Set<[Int]>()
    
    func combinate(i:Int, select:[Int]) {
        if select.count == banned_id.count {
            answerSet.update(with: select.sorted())
            return
        }
        var select = select
        
        let arr = banIdIndex[i]
        
        for n in arr {
            if select.contains(n){
                continue
            }
            select.append(n)
            combinate(i: i+1, select: select)
            select.removeLast()
        }
    }
    
    combinate(i: 0, select: [])
    
    
    return answerSet.count

}

func compareId(_ user: String, _ banId: String) -> Bool {
    
    if user.count != banId.count { return false }
    
    let u = user.map{String($0)}
    
    let b = banId.map{String($0)}
    
    for (idx,char) in b.enumerated() {
        if char != "*" && u[idx] != b[idx] {
            return false
        }
    }
    return true
}

func findingBanId(_ userId: [String], _ banId: [String]) -> [[Int]] {
    
    var banArr = Array(repeating: [Int]() , count: banId.count)
    
    for (i,user) in userId.enumerated() {
        for (j,id) in banId.enumerated() {
            
            if compareId(user, id) {
                banArr[j].append(i)
            }
        }
    }
    
    return banArr
}





print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
