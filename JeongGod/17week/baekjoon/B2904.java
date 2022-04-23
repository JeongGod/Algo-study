import java.io.*;
import java.util.*;

public class B2904 {
    static int SIZE = 78498;
    static int[] prime = new int[SIZE];
    public static int factorization(long n, int target) {
        int result = 0;
        while(n%target == 0) {
            n /= target;
            result += 1;
        }
        return result;
    }

    public static void primeSearch() {
        int idx = 0;
        for (int i=2; i<1000000; i++) {
            boolean flag = true;
            for (int j=2; j<=Math.sqrt(i); j++) {
                if (i%j == 0) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                prime[idx++] = i;
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;

        primeSearch();
        int n = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());

        int[] nums = new int[n];
        // 소수가 몇 개 사용되었는지 체크
        int[] cnts = new int[SIZE];
        List<HashMap<Integer, Integer>> list = new ArrayList<>();
        for (int i=0; i<n; i++) {
            int num = Integer.parseInt(st.nextToken());
            HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
            nums[i] = num;
            for (int j=0; j<SIZE; j++) {
                if (num < prime[j]) break;
                int cnt = factorization(num, prime[j]);
                if (cnt == 0) continue;

                map.put(prime[j], cnt);
                cnts[j] += cnt;
            }
            list.add(map);
        }

        int answer_cnt = 0;
        long answer_val = 1;
        // 소수가 몇 개 사용되었는지 돌아본다.
        for (int i=0; i<SIZE; i++) {
            int result = cnts[i] / n;
            if (result >= 1) {
                // i번째 소수는 최대공약수에 들어간다.
                answer_val *= Math.pow(prime[i], result);
                for (int j=0; j<n; j++) {
                    int tmp = list.get(j).getOrDefault(prime[i], 0);
                    if (tmp < result) {
                        answer_cnt += (result - tmp);
                    }
                }
            }
        }
        System.out.println(answer_val + " " + answer_cnt);
    }

}
