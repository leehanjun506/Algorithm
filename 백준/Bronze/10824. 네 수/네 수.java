    import java.util.*;
    import java.io.*;
    public class Main {
    	public static void main(String[] args) throws IOException {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	String[]st=new String[4];
    	st=br.readLine().split(" ");
    	String a=st[0]+st[1];
    	long a1=Long.parseLong(a);
    	String b=st[2]+st[3];
    	long b1=Long.parseLong(b);
    	bw.write(Long.toString(a1+b1));
    	bw.flush();
 }	
}