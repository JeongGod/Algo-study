import java.io.*;
import java.util.*;

public class Main {
    static int answer = 0;
    static int N, L, R, X;
    public static void pickProblems(int[] problems, int picks, int idx, int psum, int first, int last) {
        if (idx == N) {
            if (picks >= 2 && L <= psum && psum <= R && (last - first) >= X) {
                answer++;
            }
            return;
        }
        pickProblems(problems, picks, idx+1, psum, first, last);
        // 처음 고르는 경우
        if (first == 0) first = problems[idx];
        pickProblems(problems, picks+1, idx+1, psum + problems[idx], first, problems[idx]);

    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;
        st = new StringTokenizer(br.readLine());


        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        X = Integer.parseInt(st.nextToken());

        int[] problems = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            problems[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(problems);

        pickProblems(problems, 0, 0, 0, 0, 0);
        System.out.println(answer);
    }
}
