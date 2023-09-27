package array_hash;


public class CompressBad_1_5 {

    public static String compressBad(String str) {
        String mystr = "";
        char last = str.charAt(0);
        int count = 1;
        for (int i = 1; i < str.length() ; i++) {
            if (str.charAt(i) == last) {
                count++;
            } else {
                mystr += last + "" + count;
                last = str.charAt(i);
                count = 1;
            }
            
        }
        return mystr + last + count;
    }

    public static String compressBetter(String str){
        int size = countCompression(str);
        if (size >= str.length()){
            return str;
        }

        StringBuffer mystr = new StringBuffer();
        char last = str.charAt(0);
        int count =1;
        
        for(int i =1; i < str.length() ; i++){
            if(str.charAt(i) == last){
                count++;
            } else {
                mystr.append(last);
                mystr.append(count);
                last = str.charAt(i);
                count = 1;
            }
        }
        mystr.append(last);
        mystr.append(count);
        return mystr.toString();
    }
    
    public static int countCompression(String str){

        if (str == null || str.isEmpty()) return 0;

        char last = str.charAt(0);
        int size = 0;
        int count = 1;
        for(int i = 1; i < str.length(); i++){
            if(str.charAt(i) == last) {
                count++;
            } else {
                last = str.charAt(i);
                size += 1 + String.valueOf(count).length();
                count = 1;
            }
            
        }
        size += 1 + String.valueOf(count).length();
        return size;
    }

 public static void main(String[] args) {
    String str = "aaabbbccc";
    String str2 = "aabbcc";
    String str3 = "abc";
    String str4 = "a";
    String str6 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";

    System.out.println(str);
    System.out.println(compressBad(str));
    System.out.println(str2);
    System.out.println(compressBad(str2));
    System.out.println(str3);
    System.out.println(compressBad(str3));
    System.out.println(str4);
    System.out.println(compressBad(str4));
    System.out.println(str6);
    System.out.println(compressBad(str6));

    // test compressBetter
    System.out.println(str);
    System.out.println(compressBetter(str));
    System.out.println(str2);
    System.out.println(compressBetter(str2));
    System.out.println(str3);
    System.out.println(compressBetter(str3));
    System.out.println(str4);
    System.out.println(compressBetter(str4));
    System.out.println(str6);
    System.out.println(compressBetter(str6));

    }

}


