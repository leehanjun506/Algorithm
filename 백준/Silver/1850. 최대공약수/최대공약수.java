    import java.util.*;
    import java.io.*;
    public class Main {
    	static long gcd(long c,long d) {
    		long tmp=c%d;
    		return tmp==0?d:gcd(d,c%d);
    	}
    	public static void main(String[] args) throws IOException {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    		String buf[]=br.readLine().split(" ");
    		long a=Long.parseLong(buf[0]);
    		long b=Long.parseLong(buf[1]);
    		long c=Math.max(a, b);
    		long d=Math.min(a, b); 
    		long x=gcd(c,d);
    		StringBuilder x1=new StringBuilder();
    		for(long i=0;i<x;i++){
    			x1.append("1");
    		}
    		bw.write(x1.toString());
    	bw.flush();
}
    }