import java.io.*;
import java.util.*;

public class Main {
    static HashMap<Integer, Integer> connect;
    static ArrayList<ArrayList<Integer>> graph;
    static ArrayList<Integer> answer = new ArrayList<>();
    public static void dfs(int cur) {
        int cnt = connect.getOrDefault(cur, 0);
        if (cnt == 0) {
            answer.add(cur);
            for (int next : graph.get(cur)) {
                connect.put(next, connect.get(next) - 1);
                dfs(next);
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        int N, M;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        connect = new HashMap<>();
        graph = new ArrayList<>();

        for (int i=0; i<=N; i++) {
            graph.add(new ArrayList<>());
        }

        // 그래프를 만든다.
        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int before = Integer.parseInt(st.nextToken());
            for (int j=1; j<n; j++) {
                int cur = Integer.parseInt(st.nextToken());
                graph.get(before).add(cur);
                connect.put(cur, connect.getOrDefault(cur, 0) + 1);
                before = cur;
            }
        }

        // 루트점부터 파고든다.
        for (int i=1; i<=N; i++) {
            if (!connect.containsKey(i)) {
                dfs(i);
            }
        }
        if (answer.size() != N) System.out.println(0);
        else {
            for (int i : answer) System.out.println(i);
        }
    }
}

