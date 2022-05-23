//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/05/21.
//  LeetCode 200. Number of Islands

import Foundation

class Solution {
    let dx = [-1, 1, 0, 0]
    let dy = [0, 0, -1, 1]
    func numIslands(_ grid: [[Character]]) -> Int {

        var grid = grid
        var answer = 0
        
        for i in 0..<grid.count {
            for j in 0..<grid[i].count {
                if grid[i][j] == "1" {
                    bfs(&grid, i, j)
                    answer += 1
                }
            }
        }

        return answer
    }

    func bfs(_ grid: inout [[Character]], _ x: Int, _ y: Int) {
        var queue: [(Int, Int)] = [(x,y)]
        grid[x][y] = "0"
        
        var index = 0

        while index < queue.count {

            let r = queue[index].0
            let c = queue[index].1

            for i in 0..<4 {
                let nx = r + dx[i]
                let ny = c + dy[i]

                if 0 > nx || nx >= grid.count || 0 > ny || ny >= grid[0].count { continue }
                if grid[nx][ny] != "1" { continue }

                grid[nx][ny] = "0"
                queue.append((nx,ny))
            }

            index += 1
        }
        
    }

}
