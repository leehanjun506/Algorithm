import java.util.*;
public class Main {
public static void main(String []args){
    Scanner sc=new Scanner(System.in);
    int a=sc.nextInt();
    int b=sc.nextInt();
    boolean arr[]=new boolean[b+1];
    arr[0]=arr[1]=true;
    for(int i=2;i*i<=b;i++) {
    	if(!arr[i]) {
    for(int j=i*i;j<=b;j+=i) arr[j]=true;
    	}
}
    for(int i=a;i<=b;i++) {
    	if(!arr[i])
    	System.out.println(i);
}
}
}