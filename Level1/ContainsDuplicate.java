package Level1;
import java.util.*;

// https://leetcode.com/problems/contains-duplicate/
// 20220912
public class ContainsDuplicate {

    public static void main(String[] args) {
        
        int[] nums = {1,2,3,1};
        
        System.out.println("result: " + containsDuplicate(nums));
    }

    public static boolean containsDuplicate(int[] nums) {
        
        HashSet<Integer> list = new HashSet<Integer>();
        
        for(int num : nums){
            list.add(num);    
        }
        if(list.size() != nums.length)
            return true;
        else
            return false;
    }
}