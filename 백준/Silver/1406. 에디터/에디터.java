    import java.util.*;
    import java.io.*;
    public class Main {

    	public static void main(String[] args) throws IOException {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	String a=br.readLine();
    	StringBuilder a8=new StringBuilder();
    	Stack <Character> st1=new Stack<>();
    	Stack <Character> st2=new Stack<>();
    	for(int i=0;i<a.length();i++) {
    		st1.add(a.charAt(i));
    	}
    	int num=Integer.parseInt(br.readLine());
    	for(int j=0;j<num;j++) {
    		String[]buf=br.readLine().split(" ");
    		if(buf[0].equals("P")) {
    			st1.add(buf[1].charAt(0));
    			}
    		else if(buf[0].equals("L")) {
    			if(st1.isEmpty())
    				continue;
    			st2.add(st1.pop());
    		}
    		else if(buf[0].equals("D")) {
    			if(st2.isEmpty())
    				continue;
    			st1.add(st2.pop());
    		}
    		else {
    			if(st1.isEmpty())
    				continue;
    			st1.pop();
    		}
    	}
    	while(!st1.isEmpty())
    		st2.add(st1.pop());
    	while(!st2.isEmpty())
    		bw.write(st2.pop());
    	bw.flush();
}
    }