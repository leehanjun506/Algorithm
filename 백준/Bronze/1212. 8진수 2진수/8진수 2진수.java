    import java.util.*;
    import java.io.*;
    public class Main {

    	public static void main(String[] args) throws IOException {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	String a=br.readLine();
    	StringBuilder a8=new StringBuilder();
    	for(int i=0;i<a.length();i++) {
    		int x1=a.charAt(i)-48;
    		if(x1==0||x1==1)
    			a8.append("00");
    		else if(x1==2||x1==3)
    			a8.append("0");
    		a8.append(Integer.toBinaryString(x1));
    		
    	}
    	if(a.charAt(0)=='0'||a.charAt(0)=='1')
    		System.out.print(a8.substring(2));
    	else if(a.charAt(0)=='2'||a.charAt(0)=='3')
    		System.out.print(a8.substring(1));
    	else
    		System.out.print(a8);
 
    	
}
    }