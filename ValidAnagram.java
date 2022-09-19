import java.util.*;

public class ValidAnagram {

    //https://leetcode.com/problems/valid-anagram/

    public static void main(String[] args) {
//        String s = "anagram";
//        String t = "nagaram";

        String s = "cat";
        String t = "car";

        System.out.println("result: " + isAnagram(s, t));
    }

    public static boolean isAnagram(String s, String t) {
        boolean result = true;
        if (s.length() != t.length()) return false;
        
        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();

        Arrays.sort(sArray);
        Arrays.sort(tArray);

        for (int i = 0; i < sArray.length; i++) {
            char sChar = sArray[i];
            char tChar = tArray[i];

            if (sChar != tChar) {
                result = false;
                break;
            }
        }
        return result;
    }
}
