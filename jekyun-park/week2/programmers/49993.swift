//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/01/06.
//

import Foundation


func solution(_ skill:String, _ skill_trees:[String]) -> Int {
    var answer = 0
    
    for tree in skill_trees {
        let list = tree.filter{ skill.contains($0) }
        let prefix = skill.prefix(list.count)
        print(list,prefix)
        if prefix == list { answer += 1}
    }
    
    return answer
}

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
