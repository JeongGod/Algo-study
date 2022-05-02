import java.io.*;
import java.util.*;

public class Main {
    static int[] root;

    public static int find(int x) {
        if (x == root[x]) return x;
        root[x] = find(root[x]);
        return root[x];
    }

    public static void union(int x, int y) {
        if (x < y) root[x] = y;
        else root[y] = x;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;
        // 같은 부모를 바라보고 있으면 Cycle
        int N, M;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        root = new int[N];
        for (int i=0; i<N; i++) root[i] = i;


        for (int i=0; i<M; i++) {
            int x, y;
            st = new StringTokenizer(br.readLine());
            x = Integer.parseInt(st.nextToken()); y = Integer.parseInt(st.nextToken());

            int px = find(x), py = find(y);
            if (px == py) {
                System.out.println(i+1);
                return;
            }
            union(px, py);
        }
        System.out.println(0);
    }
}

