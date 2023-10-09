package Level1;

public class UniqueString {

    // 문자열에 포함된 문자들이 전부 유일한지를 검사하는 알고리즘을 구현하라. 다른 자료구조를 사용할 수 없는 상황이라면 어떻게 할건가?
    public static void main(String[] args) {
        
        System.out.println(checkUniqueLetter("akasjdfsdf")); 

    }

    public static boolean checkUniqueLetter(String str){
        if(str.length() > 256 ) return false;

        boolean[] char_set = new boolean[256];

        for(int i=0; i< str.length(); i++){
            char val = str.charAt(i);
            if(char_set[val])   // check include letter
                return false;
            
            char_set[val] = true;
        }

        return true;

    }
    
}
