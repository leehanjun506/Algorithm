    import java.util.*;
    import java.io.*;
    public class Main {
    	
    	public static void main(String[] args) throws IOException {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	String input;
    	int a=0,b=0,c=0,d=0;
    	while((input=br.readLine())!=null) {
    		for(int i=0;i<input.length();i++) {
    			if(input.charAt(i)>='a'&&input.charAt(i)<='z')
    				a++;
    			else if(input.charAt(i)>='A'&&input.charAt(i)<='Z')
    				b++;
    			else if(input.charAt(i)>='0'&&input.charAt(i)<='9')
    				c++;
    			else if(input.charAt(i)==' ')
    				d++;
    		}
	    	bw.write(a+" "+b+" "+c+" "+d+"\n");
	    	bw.flush();
	    	a=0;b=0;c=0;d=0;
    	}

 }	
}