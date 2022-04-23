import java.util.*;

class Node implements Comparable<Node>{
    int dest, cost;

    public Node(int dest, int cost) {
        this.dest = dest;
        this.cost = cost;
    }

    @Override
    public int compareTo(Node o) {
        if (this.cost > o.cost) return 1;
        else if (this.cost == o.cost) return 0;
        else return -1;

    }
}

class Solution {
    public int solution(int n, int[][] costs) {
        ArrayList<ArrayList<Node>> graph = new ArrayList<>();
        for (int i=0; i<n; i++) graph.add(new ArrayList<>());

        for (int[] ints : costs) {
            int x = ints[0];
            int y = ints[1];
            int cost = ints[2];

            graph.get(x).add(new Node(y, cost));
            graph.get(y).add(new Node(x, cost));
        }

        PriorityQueue<Node> pq = new PriorityQueue<>();
        boolean[] visited = new boolean[n];


        pq.add(new Node(0, 0));
        int answer = 0;
        while (!pq.isEmpty()) {
            Node cur = pq.poll();
            if (visited[cur.dest]) continue;
            visited[cur.dest] = true;

            answer += cur.cost;

            for (Node ns : graph.get(cur.dest)) {
                if (visited[ns.dest]) continue;
                pq.add(new Node(ns.dest, ns.cost));
            }
        }
        return answer;

    }
}

public class P42861 {
    public static void main(String[] args) {
        System.out.println(new Solution().solution(4, new int[][] {{0,1,1},{0,2,2},{1,2,5},{1,3,1},{2,3,8}}));
    }
}