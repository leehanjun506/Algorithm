    import java.util.*;
    import java.io.*;
    public class Main {

    	public static void main(String[] args) throws IOException {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	int num=Integer.parseInt(br.readLine());
    		int x=2;
    		while(num!=1) {
    			if(num%x==0) {
    				System.out.println(x);
    			num=num/x;}
    			else {
    				x++;
    			}
    		}
    	
    	
}
    }