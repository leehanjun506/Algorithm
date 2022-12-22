    import java.util.*;
    import java.io.*;
    public class Main {

    	public static void main(String[] args) throws IOException {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	int num=Integer.parseInt(br.readLine());
    	Stack <Integer> st=new Stack<>();
    	if(num==0)
    		System.out.print("0");
    	while(num!=0) {
    		if(num%-2<0) {
    			num=(num/-2)+1;
    			st.push(1);
    			
    		}
    		else {
    			st.push(num%-2);
    			num/=-2;
    			
    	}
    	}
    	int x=st.size();
    	for(int i=0;i<x;i++) {
    		System.out.print(st.pop());
    	}
}
    	}