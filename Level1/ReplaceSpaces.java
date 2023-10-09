package Level1;

public class ReplaceSpaces {
// Assume string has sufficient free space at the end
public static void replaceSpaces(char[] str, int trueLength) {
    int spaceCount = 0, index, i = 0;
    for (i = 0; i < trueLength; i++) {
        if (str[i] == ' ') {
            spaceCount++;
        }
    }
    index = trueLength + spaceCount * 2;
    if (trueLength < str.length) str[trueLength] = '\0';
    for (i = trueLength - 1; i >= 0; i--) {
        if (str[i] == ' ') {
            str[index - 1] = '0';
            str[index - 2] = '2';
            str[index - 3] = '%';
            index = index - 3;
        } else {
            str[index - 1] = str[i];
            index--;
        }
    }
}

public static int findLastCharacter(char[] str) {
    for (int i = str.length - 1; i >= 0; i--) {
        if (str[i] != ' ') {
            return i;
        }
    }
    return -1;
}

public static void main(String[] args) {
    String str = "Mr John Smith    ";
    char[] arr = str.toCharArray();
    int trueLength = findLastCharacter(arr) + 1;
    replaceSpaces(arr, trueLength);	
    //System.out.println("\"" + AssortedMethods.charArrayToString(arr) + "\"");
}

    // public static void main(String[] args) {
    //     String str = "inam dfiew wsdlfkj";
    //     replaceSpaces(str.toCharArray(), str.length());

    // }
    
    // public static void replaceSpaces(char[] str, int length){
    //     int spaceCount = 0, newLength, i= 0;
    //     // 1. how many space in string
    //     for(i=0; i<length ; i++){
    //         if(str[i] == ' ' ){
    //             spaceCount++;
    //         }
    //     }
    //     newLength = length + spaceCount * 2;
    //     if(newLength < length)
    //         str[newLength] = '\0';

    //     //2. change space to '%20'
    //     for(i = newLength-1 ; i >=0 ; i--){
    //         if(str[i] == ' '){
    //             str[newLength-1] = '0';
    //             str[newLength-2] = '2';
    //             str[newLength-3] = '%';
    //             newLength = newLength - 3;
    //         }else{
    //             str[newLength-1] = str[i];
    //             newLength = newLength - 1;
    //         }
    //     }
    // }
}
