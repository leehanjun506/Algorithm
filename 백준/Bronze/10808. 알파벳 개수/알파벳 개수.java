import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int arr[] = new int[26];
        int num;
        String s1 = br.readLine();
        char[] s2 = s1.toCharArray();
        for (int i = 0; i < s2.length; i++) {
            num = s2[i]-'a';
            arr[num]+=1;
        }
        for (int i = 0; i < arr.length; i++) {
            bw.write(arr[i]+" ");
        }
        bw.flush();
        br.close();
        bw.close();
        
    }
}
