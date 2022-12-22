    import java.util.*;
    import java.io.*;
    public class Main {

    	public static void main(String[] args) throws IOException {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	String a=br.readLine();
    	StringBuilder b=new StringBuilder(a).reverse();
    	StringBuilder a8=new StringBuilder();
    	int n=0;
    	int x3=0;
    	for(int i=0;i<b.length();i++) {
    		if(n==0) {
    			x3+=(int)b.charAt(i)-48;
    			n++;
    			if(i==b.length()-1)
    				a8.append(x3);
    		}
    		else if(n==1) {
    			x3+=2*(int)(b.charAt(i)-48);
    			n++;
    			if(i==b.length()-1)
    				a8.append(x3);
    		}
    		else  {
    			x3+=4*(int)(b.charAt(i)-48);
    			a8.append(x3);
    			n=0;
    			x3=0;
    		}
    	}
    	System.out.print(a8.reverse());
    	bw.flush();
 
    	
}
    }