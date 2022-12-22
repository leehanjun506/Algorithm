    import java.util.*;
    import java.io.*;
    public class Main {
    	static int list[]=new int[1000001];
    	static int[] gold(int n) {
    		boolean arr[]=new boolean[n+1];
    		arr[0]=true;
    		arr[1]=true;
    		for(int i=2;i*i<=n;i++) {
    			if(!arr[i]) {
    				for(int j=i*i;j<=n;j+=i) {
    					arr[j]=true;
    				}
    			}
    		}
    		arr[2]=true;
    		for(int i=0;i<=n;i++) {
    			if(!arr[i])
    				list[i]=i;
    		}
    		return list;
    	}
  
    	public static void main(String[] args) throws IOException {
    	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
    	int []arr=new int[1000001];
    	arr=gold(1000001);
    	while(true) {
    		int flag=0;
    		int n=Integer.parseInt(br.readLine());
    		if(n==0)
    			break;
    		
    		for(int i=3;i<n;i+=2) {
    			if(arr[i]!=0&&arr[n-i]!=0) {
    				bw.write(n+" = "+arr[i]+" + "+arr[n-i]+"\n");
    				flag=1;
    				break;
    			}
    		}
    		if(flag==0)
    			bw.write("Goldbach's conjecture is wrong.\n");
    		}
    	bw.flush();
}
    	}
    