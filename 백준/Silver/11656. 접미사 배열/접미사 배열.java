    import java.util.*;
    import java.io.*;
    public class Main {
    	public static void main(String[] args) throws IOException {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	String st=br.readLine();
    	String [] buf=st.split("");
    	buf[st.length()-1]=Character.toString(st.charAt(st.length()-1));
    	for(int i=st.length()-2;i>=0;i--) {
    		buf[i]+=buf[i+1];
    	}
    	Arrays.sort(buf);
    	for(int i=0;i<buf.length;i++) {
    		System.out.println(buf[i]);
    	}
}
    }