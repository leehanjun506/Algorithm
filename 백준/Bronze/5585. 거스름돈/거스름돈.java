import java.util.*;
public class Main {
public static void main(String []args){
    Scanner sc=new Scanner(System.in);
    int price=sc.nextInt();
    int ans=1000-price;
    int x,y,z,i,j,k;
    	x=ans/500;
    	ans%=500;
    	y=ans/100;
    	ans%=100;
        k=ans/50;
        ans%=50;
    	z=ans/10;
    	ans%=10;
        i=ans/5;
        ans%=5;
        j=ans/1;
        ans%=1;
    System.out.print(x+y+z+i+j+k);
}
}