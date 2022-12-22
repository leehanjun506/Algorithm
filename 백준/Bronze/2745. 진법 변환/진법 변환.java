    import java.util.*;
    import java.io.*;
    public class Main {

    	public static void main(String[] args) throws IOException {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	String[] s=br.readLine().split(" ");
    	String a=s[0];
    	int x=0;
    	int num;
    	int b=Integer.parseInt(s[1]);
    	long sum=0;
    	for(int i=a.length()-1;i>=0;i--) {
    		if(a.charAt(i)>='A'&&a.charAt(i)<='Z') 
    			num=(int)(a.charAt(i)-55);
    		else 
    			num=(int)(a.charAt(i)-48);
    		sum+=num*Math.pow(b, x);
    		x++;
    	}
    	bw.write(Long.toString(sum));
    	bw.flush();
 
    	
}
    }