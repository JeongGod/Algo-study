//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/01/07.
//

import Foundation

func solution(_ n:Int, _ computers:[[Int]]) -> Int {
    
    var answer: Int = 0
    var visited: [Bool] = Array(repeatElement(false, count: n+1)) // visited = [false , false , false , ... ]
    var graph: [[Int]] = Array(repeating: [], count: n+1) // graph = [ [] , [1,2,3,...,n] , [1,2,3,...,n] , ... , [1,2,3,...,n] ] -> graph[i] -> i 번째 컴퓨터와 연결된 컴퓨터들의 배열
    
    for i in 1..<n+1{
        for j in 0..<n{
            if computers[i-1][j] == 1 {
                graph[i].append(j+1)
            }
        }
    }
    
    func bfs(_ startComputer: Int) -> Int {
        var que = [startComputer] // startComputer -> 시작한 컴퓨터 번호, 큐에 시작한 컴퓨터 번호 넣고 시작
        
        if visited[startComputer] == true {
            return 0
        }
        
        visited[startComputer] = true
        
        while !que.isEmpty {
            let v = que.removeFirst() // 1
            for i in graph[v] { // 1번 컴퓨터와 연결된 컴퓨터들 ~ ~> 큐에 넣고 방문처리 ~> 큐에서 pop한다음 해당 컴퓨터와 연결된 컴퓨터들 큐에 넣고 방문처리 ~> 반복 ~> 큐가 빌때까지
                if visited[i] == false { //
                    que.append(i)
                    visited[i] = true
                }
            }
        }
        return 1
    }
    
    for i in 1...n {
        answer += bfs(i)
    }
    
    return answer
}

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

// 어 렵 다 ! 
