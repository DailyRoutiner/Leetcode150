public class CompressBad {
    public static void main(String[] args) {
        
        System.out.println(compressBad("aabcccccccdddddda")); 
    }

    public static String compressBad(String str){
        StringBuffer mystr = new StringBuffer();
        char last = str.charAt(0);
        int count = 1;

        // This algorithm has a problem. O(n2)
        for(int i = 1; i < str.length() ; i++){
            if(str.charAt(i) == last)
                count++;
            else{
                mystr.append(last).append(count);
                //mystr += str.charAt(i-1) + "" + count;
                last = str.charAt(i);
                count = 1;
            }
        }
        
        return mystr.append(last).append(count).toString();
    }
}
