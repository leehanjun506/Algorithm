    import java.util.*;
    import java.io.*;
    public class Main {

    	public static void main(String[] args) throws IOException {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	String num[]=br.readLine().split(" ");
    	Stack<Integer>st=new Stack<>();
    	int a=Integer.parseInt(num[0]);
    	int b=Integer.parseInt(num[1]);
    	int sum=0;
    	int m=Integer.parseInt(br.readLine());
    	String num1[]=br.readLine().split(" ");
    	int x[]=new int[m];
    	int r=m;
    	for(int i=0;i<r;i++) {
    		x[i]=Integer.parseInt(num1[i]);
    		sum+=x[i]*Math.pow(a, m-1);
    		m--;
    	}
    	while(sum!=0) {
    		st.push(sum%b);
    		sum/=b;
    	}
    	int aa=st.size();
    	for(int i=0;i<aa;i++) {
    		System.out.print(st.pop()+" ");}
    	}
    	
}
    	