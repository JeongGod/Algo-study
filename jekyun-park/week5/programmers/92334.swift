//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/01/27.
//

import Foundation

func solution(_ id_list: [String], _ report: [String], _ k: Int) -> [Int] {

    var countDictionary: [String: Set<String>] = [:]
    var reportDictionary: [String: [String]] = [:]
    var answer: [Int] = []
    
    id_list.forEach {
        countDictionary[$0] = []
        reportDictionary[$0] = []
    }

    for content in report {
        let splitted = content.split(separator: " ")
        let reporter = String(splitted[0])
        let banned = String(splitted[1])
        countDictionary[banned]!.insert(reporter)
        if !reportDictionary[reporter]!.contains(banned) {
            reportDictionary[reporter]?.append(banned)
        }
    }

    id_list.forEach { answer.append((reportDictionary[$0]?.filter { countDictionary[$0]!.count >= k }.count)! ) }
    
    return answer
}

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))

//print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
