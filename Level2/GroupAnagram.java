package Level2;
import java.lang.reflect.Array;
import java.util.*;

public class GroupAnagram {
    
    public static void main(String[] args) {
        String[] str = {"eat","tea","tan","ate","nat","bat"};

       System.out.println(groupAnagrams(str)) ; 

    }
    
    public static List<List<String>> groupAnagrams(String[] strs) {
        
        List<List<String>> strList = new ArrayList<>();
        HashMap<String, List<String>> map = new HashMap<>();
        for(int i = 0 ; i < strs.length ; i++){
            
            String str = strs[i];       // eat tea

            char[] arrC = str.toCharArray();
            Arrays.sort(arrC);          // aet  ... key
            
            String temp = new String(arrC);

            if(map.containsKey(temp)){   // matching key
                map.get(temp).add(str);  // eat

            }else{
                List<String> list = new ArrayList<>();
                list.add(str);
                strList.add(list);
                map.put(temp, list);
            }

        }
        return strList;

    }

}
