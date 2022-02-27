//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2021/12/22.
//


// refactor plz...

import Foundation


func solution(_ record:[String]) -> [String] {
    let newRecord = record.map { $0.split(separator: " ") }
    var dictionary : [String:(String,Bool)] = [:]
    var users : [(String,Bool)] = []
    var answer : [String] = []
    
    
    for element in newRecord {
        if (element[0] == "Enter") {
            dictionary[String(element[1])] = (String(element[2]),true)
            users.append((String(element[1]),true))
        } else if (element[0] == "Leave"){
            dictionary[String(element[1])] = (String(dictionary[String(element[1])]!.0) ,false)
            users.append((String(element[1]),false))
        } else { // change
            dictionary[String(element[1])] = (String(element[2]),Bool(dictionary[String(element[1])]!.1))
        }
    }
    
    for user in users {
        if user.1 == true{
            answer.append(dictionary[user.0]!.0+"님이 들어왔습니다.")
        } else {
            answer.append(dictionary[user.0]!.0+"님이 나갔습니다.")
        }
    }
    return answer
}




