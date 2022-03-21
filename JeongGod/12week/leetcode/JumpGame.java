import java.util.*;

class JumpGame {
    public boolean canJump(int[] nums) {
        int maxIdx = 0;
        if (nums.length == 1) return true;
        Deque<List<Integer>> dq = new ArrayDeque<>();
        dq.addLast(Arrays.asList(0, nums[0]));

        while (dq.size() > 0) {
            List<Integer> result = dq.removeFirst();
            int cur = result.get(0);
            int maxJump = result.get(1);

            for (int i=maxIdx+1; i<=cur+maxJump; i++) {
                if (i >= nums.length-1) {
                    return true;
                }

                dq.addLast(Arrays.asList(i, nums[i]));
            }

            maxIdx = Math.max(maxIdx, cur+maxJump);
        }
        return false;
    }
}