package Level2;

import java.util.*;

// https://leetcode.com/problems/top-k-frequent-elements/
public class TopFrequentElements {
    
    public static void main(String[] args) {
        
        int[]nums = {1,1,1,2,2,3};
        int k = 2;

        topKFrequent(nums, k);
    }

    public static int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] ans = new int[k];
        
        for(int num : nums){
            if(map.containsKey(num)){
                map.put(num, map.get(num) + 1);
            }else{
                map.put(num, 1);
            }
        }
        //Solution2
        List<Integer> list = new ArrayList<>(map.keySet());
        Collections.sort(list, (a,b) -> map.get(b) - map.get(a));        

        for(int i = 0; i < k ; i++){
            // int max = findMax(map);
            // ans[i] = max;
            // map.remove(max);
            
            ans[i] = list.get(i);
        }
        return ans;
    }

    // Solution1
    private static int findMax(HashMap<Integer, Integer> map) {
        int val=0, max = 0;
        for(Map.Entry<Integer,Integer> key : map.entrySet()){
            if(max < key.getValue()){
                val = key.getKey();
                max = key.getValue();
            }
        }
        return val;
    }
}
