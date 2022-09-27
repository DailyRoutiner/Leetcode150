package Level1;

public class ValidPalindrome {    

    public static void main(String[] args) {
       System.out.println(isPalindrome("A man, a plan, a canal: Panama")); 
    }

    
    public static boolean isPalindrome(String s) {
        boolean ans = true ;
        // replace all non-Charaters
        s = s.toLowerCase().replaceAll("[^A-Za-z0-9]", "");
        // compare i, j index
        for(int i=0, j=s.length()-1 ;i <= j; i++, j--){
           if(s.charAt(i) != s.charAt(j) ){
                return false;
           }
        }

        return ans;
    }
    
}
