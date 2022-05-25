import java.util.*;

class Solution {
    public int[] solution(String msg) {
        ArrayList<Integer> answer = new ArrayList<>();

        HashMap<String, Integer> hashMap = new HashMap<>();

        /**
         * 1. 알파벳 순서대로 해쉬맵에 담는다.
         * 2. 만약 해당 알파벳이 해쉬맵에 존재한다면 다음것도 확인한다.
         * 3. 존재하지 않는다면 해당 알파벳을 추가하고, 그 전까지 포인터를 옮긴다.
         */
        for (char i = 'A'; i <= 'Z'; i++) {
            hashMap.put(String.valueOf(i), i - 'A' + 1);
        }
        int pointer = 0;
        while (true) {
            String result = "";
            while (pointer < msg.length() && hashMap.containsKey(result.concat(String.valueOf(msg.charAt(pointer))))) {
                result = result.concat(String.valueOf(msg.charAt(pointer)));
                pointer++;
            }
            answer.add(hashMap.get(result));
            if (pointer == msg.length()) break;
            hashMap.put(result.concat(String.valueOf(msg.charAt(pointer))), hashMap.size()+1);
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }

}