import java.util.*;
class Solution {
    public int solution(int n, int s, int a, int b, int[][] fares) {
        int answer = Integer.MAX_VALUE;
        int[][] graph = new int[n][n];
        
        for (int i=0; i<n; i++) {
            Arrays.fill(graph[i], 1000000);
            
            graph[i][i] = 0;
        }
        for (int[] x : fares) {
            graph[x[0]-1][x[1]-1] = x[2];
            graph[x[1]-1][x[0]-1] = x[2];
        }
        
        for (int k=0; k<n; k++) {
            for (int i=0; i<n; i++) {
                for (int j=0; j<n; j++) {
                    graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
                }
            }
        }

        
        for (int i=0; i<n; i++) {
            answer = Math.min(answer, graph[s-1][i] + graph[i][a-1] + graph[i][b-1]);
        }
        
        return answer;
    }
}