    import java.util.*;
    import java.io.*;
    public class Main {
    	static int gcd(int c,int d) {
    		long tmp=c%d;
    		return tmp==0?d:gcd(d,c%d);
    	}
    	public static void main(String[] args) throws IOException {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	int input=Integer.parseInt(br.readLine());
 
    	for(int i=0;i<input;i++) {
    		long sum=0;
    		String[] n=br.readLine().split(" ");
    		int num=Integer.parseInt(n[0]);
    		for(int j=1;j<num+1;j++) {
    			for(int k=num;k>j;k--) {
    				int a=Math.max(Integer.parseInt(n[j]), Integer.parseInt(n[k]));
    				int b=Math.min(Integer.parseInt(n[j]), Integer.parseInt(n[k]));
    				sum+=gcd(a,b);
    			}
    		}
        	bw.write(Long.toString(sum));
        	bw.newLine();
    	}
    	bw.flush();
}
    }