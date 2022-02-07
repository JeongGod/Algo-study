//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/02/03.
//

import Foundation

func solution(_ info: [String], _ query: [String]) -> [Int] {

    var answer: [Int] = []
    var dictionary: [String: [Int]] = [:]

    for data in info {
        let splittedData = data.components(separatedBy: .whitespaces)
        let language = [splittedData[0], "-"]
        let job = [splittedData[1], "-"]
        let career = [splittedData[2], "-"]
        let soulFood = [splittedData[3], "-"]
        let score = Int(splittedData[4])!

        for a in language {
            for b in job {
                for c in career {
                    for d in soulFood {
                        let key = "\(a) \(b) \(c) \(d)"
                        if dictionary.keys.contains(key) {
                            dictionary[key]?.append(score)
                        } else {
                            dictionary[key] = [score]
                        }
                    }
                }
            }
        }
    }

    for applicant in dictionary {
        let sortedArray = applicant.value.sorted()
        dictionary[applicant.key] = sortedArray
    }

    query.forEach {
        let splittedQuery = $0.components(separatedBy: .whitespaces)

        let language = splittedQuery[0]
        let job = splittedQuery[2]
        let career = splittedQuery[4]
        let soulFood = splittedQuery[6]
        let score = Int(splittedQuery[7])!

        let key = "\(language) \(job) \(career) \(soulFood)"

        if let findScore = dictionary[key] {
            var start = 0
            var end = findScore.count - 1

            while start <= end {
                let mid = (start + end) / 2

                if findScore[mid] < score {
                    start = mid + 1
                } else {
                    end = mid - 1
                }
            }
            answer.append(findScore.count - start)
        } else {
            answer.append(0)
        }
    }
    return answer
}

// print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))

