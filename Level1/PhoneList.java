package Level1;
import java.sql.ResultSet;
import java.util.*;

// https://school.programmers.co.kr/learn/courses/30/lessons/42577
// 20220917
class PhoneList {

    public static void main(String[] args){
        String[] str = {"119", "97674223", "1195524421"};

        System.out.println("Result : " + solution(str));
    }

    public static boolean solution(String[] phone_book) {
        boolean answer = true;
        // 1. HashMap containsKey 사용
        HashMap<String, Integer> map = new HashMap<>();
        for(String phoneNumber : phone_book){
            map.put(phoneNumber, 1);  
        }

        for(String phoneNumber : phone_book){
           for(int j=1; j < phoneNumber.length() ; j++){
                String prefix = phoneNumber.substring(0, j);
                if(map.containsKey(prefix))
                    return false;
            }
        }

        // 2. startWith 를 써서 푸는 방법
        // for(int i=0; i<phone_book.length-1; i++) {
        //     for(int j=i+1; j<phone_book.length; j++) {
        //         if(phone_book[i].startsWith(phone_book[j])) {return false;}
        //         if(phone_book[j].startsWith(phone_book[i])) {return false;}
        //     }
        // }
        // return true;
        
        return answer;
    }
}