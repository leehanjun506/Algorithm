import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] alp = new int[26];
        Arrays.fill(alp,-1);
        String s = br.readLine();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int num = c - 'a';
            if (alp[num] != -1) {
                continue;
            }
            alp[num] = i;
        }
        for (int i = 0; i < alp.length; i++) {
            bw.write(alp[i]+" ");
        }
        bw.flush();
        
    }
}