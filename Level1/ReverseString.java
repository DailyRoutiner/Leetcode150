public class ReverseString {
    public static void main(String[] args) {
        
        System.out.println(reverse("helloasdofjhasdl;fkjas;dlkfjoiefewojbfksjdlv"));
    }

    public static String reverse(String str){
        StringBuffer sb = new StringBuffer();
        
        for(int i = str.length()-1; 0 <= i ; i--){   
            sb.append(str.charAt(i));
        }

        return sb.toString();
    }
}
