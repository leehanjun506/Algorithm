    import java.util.*;
    import java.io.*;
    public class Main {
    	static int five(int n) {
    		int count1=0;
    		while(n>=5) {
    			count1+=n/5;
    			n/=5;
    		}
    		return count1;
    	}
    	static int two(int n) {
    		int count2=0;
    		while(n>=2) {
    			count2+=n/2;
    			n/=2;
    		}
    		return count2;
    	}
    	
    	public static void main(String[] args) throws IOException {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	String []s=br.readLine().split(" ");
    	int n=Integer.parseInt(s[0]);
    	int m=Integer.parseInt(s[1]);
    	int x=n-m;
    	int two=two(n)-two(m)-two(x);
    	int five=five(n)-five(m)-five(x);
    	System.out.print(Math.min(two,five));
    	}
}
    