//
//  main.swift
//  SwiftAlgorithms
//
//  Created by 박제균 on 2022/03/08.
//  LeetCode > 130. Surrounded Regions

import Foundation

class Solution {
    func solve(_ board: inout [[Character]]) {
        for i in 0..<board.count {
            for j in 0..<board[0].count {
                if board[i][j] == "O" {
                    var currendBoard = board
                    if dfs(&currendBoard, row: i, column: j) {
                        board = currendBoard
                    }
                }
            }
        }
    }

    func dfs(_ board: inout [[Character]], row: Int, column: Int) -> Bool {

        if row < 0 || row >= board.count || column < 0 || column >= board[0].count { return false }
        if board[row][column] != "O" { return true }

        board[row][column] = "X"

        for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)] {

            let nr = row + dr, nc = column + dc
            if !dfs(&board, row: nr, column: nc) { return false }
        }
        return true
    }
}

