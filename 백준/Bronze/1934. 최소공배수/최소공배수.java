    import java.util.*;
    import java.io.*;
    public class Main {
    	
    	static int gcd(int c,int d) {
    		int tmp=c%d;
    			return tmp==0?d:gcd(d,tmp);
    	}
    	static int lcm(int c,int d) {
    		int n=gcd(c,d);
    		return c*d/n;
    	}
    	
    	public static void main(String[] args) throws IOException {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	int input=Integer.parseInt(br.readLine());
    	for(int i=0;i<input;i++) {
    		String buf[]=br.readLine().split(" ");
    		int a=Integer.parseInt(buf[0]);
    		int b=Integer.parseInt(buf[1]);
    		int c=Math.max(a, b);
    		int d=Math.min(a, b);
    		bw.write(Integer.toString(lcm(c,d)));
    		bw.newLine();
    	}
    	bw.flush();
}
    }