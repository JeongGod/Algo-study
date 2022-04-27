import java.io.*;
import java.util.*;

public class Main {
    static int[] root;
    public static int find(int p) {
        if (root[p] == p) {
            return p;
        }
        root[p] = find(root[p]);
        return root[p];
    }

    public static void union(int child, int parent) {
        root[child] = root[parent];
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        int G, P;

        G = Integer.parseInt(br.readLine());
        P = Integer.parseInt(br.readLine());

        int[] airplains = new int[P];
        root = new int[G+1];
        for (int i=0; i<=G; i++) {
            root[i] = i;
        }

        int answer = 0;
        for (int i=0; i<P; i++) {
            int gate = Integer.parseInt(br.readLine());
            // 만약 부모를 찾았는데 0이면 더 이상 도킹할 수 없다는 얘기
            int parent = find(gate);
            if (parent == 0) break;
            answer++;
            union(parent, parent-1);
        }
        System.out.println(answer);

    }
}
