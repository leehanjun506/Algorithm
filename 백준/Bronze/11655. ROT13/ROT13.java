    import java.util.*;
    import java.io.*;
    public class Main {
    	public static void main(String[] args) throws IOException {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	String input=br.readLine();
    	for(int i=0;i<input.length();i++) {
    		if(input.charAt(i)<'n'&&input.charAt(i)>='a') {
    			bw.write(input.charAt(i)+13);
    		}
    		else if(input.charAt(i)>='A'&&input.charAt(i)<'N') {
    			bw.write(input.charAt(i)+13);
    		}
    		else if(input.charAt(i)<='z'&&input.charAt(i)>='n') {
    			bw.write(input.charAt(i)-13);
    		}
    		else if(input.charAt(i)>='N'&&input.charAt(i)<='Z') {
    			bw.write(input.charAt(i)-13);
    		}
    		else
    			bw.write(input.charAt(i));
    		}
    	bw.flush();
 }	
}