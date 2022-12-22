import java.io.*;
public class Main {
	static long mem[]=new long[91];
	static long fib(int n) {
		if(n==0)
			return 0;
		else if(n==1)
			return 1;
        else if(mem[n]!=0)
            return mem[n];
		else 
            mem[n]=fib(n-1)+fib(n-2);
			return mem[n];
			
	}
public static void main(String [] args)  throws IOException {
	BufferedReader bf=new BufferedReader(new InputStreamReader(System.in));
	String s=bf.readLine();
	int n= Integer.parseInt(s);
	System.out.print(fib(n));
	}
}
