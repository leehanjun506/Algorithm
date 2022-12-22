    import java.util.*;
    import java.io.*;
    public class Main {

    	static int fact(int num) {
    		if(num==0)
    			return 1;
    		
    		return num*fact(num-1);
    	}
    	public static void main(String[] args) throws IOException {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	int num=Integer.parseInt(br.readLine());
    	System.out.print(fact(num));
    	
    	
    	
}
    }