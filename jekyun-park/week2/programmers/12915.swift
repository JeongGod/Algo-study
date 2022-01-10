//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/01/06.
//

import Foundation

func solution(_ strings:[String], _ n:Int) -> [String] {
    
    var dict : [Character:[String]] = [:]
    
    for string in strings {
        let char = string[String.Index(encodedOffset: n)]
        
        if (dict[char] == nil) {
            dict[char] = []
            dict[char]?.append(string)
        } else {
            dict[char]?.append(string)
        }
    }
    
    let sortedDict = dict.sorted { a, b in
        return (a.key < b.key)
    }
    var answer :[String] = []
    
    for (key,value) in sortedDict {
        
        answer += value.sorted()
    }
    
    return answer
}

// refactor

func solution2(_ strings:[String], _ n:Int) -> [String] {
    return strings.sorted { Array($0)[n] == Array($1)[n] ? $0 < $1 : Array($0)[n] < Array($1)[n] }
}

