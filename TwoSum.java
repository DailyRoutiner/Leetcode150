import java.util.*;

public class TwoSum {
    
    public static void main(String[] args) {
        int[] nums = {3,2,4};
        int target = 6;

        System.out.println(twoSum(nums, target)); 

    }
    public static int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] ans = new int[2];

        for(int i=0; i<nums.length; i++){
            int diff = target - nums[i];
            
            if(map.containsKey(diff)){
                ans[0] = map.get(diff);
                ans[1] = i;
                break;
            }
            else{
                map.put(nums[i], i);    // value, index
            }
        }
        return ans;
    }

    // public static int[] twoSum(int[] nums, int target) {
    //     HashMap<Integer, Integer> map = new HashMap<>();
        
    //     int[] ans = new int[2];
        
    //     for(int i=0 ; i < nums.length-1; i++){
    //         for(int j=i+1; j < nums.length ; j++ ){
    //             if( target == (nums[i] + nums[j]) ){
    //                 ans[0] = i;
    //                 ans[1] = j;
    //             }
    //         }
    //     }
        
    //     return ans;
    // }
}
