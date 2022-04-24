package P12920;


class Solution {
    public long calc(int[] cores, int target) {
        long result = 0;
        for (int val : cores) {
            result += ((target / val) + 1);
        }
        return result;
    }

    public int solution(int n, int[] cores) {

        if (n <= cores.length) return n;

        int left = 1, right = (int) 5e8;
        // 시간을 구한다.
        while (left <= right) {
            int mid = (left + right) / 2;
            long result = calc(cores, mid);
            if (result < n) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }

        }
        // 구한 시간을 이용하여 몇 번째 인덱스가 마지막에 넣었는지 체크한다.
        n -= calc(cores, left-1);

        for (int i=0; i<cores.length; i++) {
            // 해당 core에 넣을 수 있다면
            if (left % cores[i] == 0) {
                n -= 1;
            }
            if (n == 0) return i+1;
        }
        return 1;
    }
}

public class P12920 {
    public static void main(String[] args) {
        System.out.println(new Solution().solution(6, new int[] {1,2,3}));
        System.out.println(new Solution().solution(5, new int[] {50, 50, 50, 30}));
    }
}
