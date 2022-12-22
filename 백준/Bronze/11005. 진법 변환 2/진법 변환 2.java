    import java.util.*;
    import java.io.*;
    public class Main {

    	public static void main(String[] args) throws IOException {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	String[] s=br.readLine().split(" ");
    	int a=Integer.parseInt(s[0]);
    	int b=Integer.parseInt(s[1]);
    	StringBuilder st=new StringBuilder();
    	while(a!=0) {
    		if(a%b>=10) {
    			st.append((char)(a%b-10+'A'));
    		}
    		else {
    			st.append((char)(a%b+'0'));
    		}
    		a=a/b;
    	}
    	bw.write(st.reverse().toString());
    	bw.flush();
 
    	
}
    }