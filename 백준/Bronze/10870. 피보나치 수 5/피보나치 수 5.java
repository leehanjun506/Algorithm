import java.util.*;
public class Main{
    static int fib(int num){
    if(num==0)
    return 0;
    else if(num==1)
    return 1;
    else
    return fib(num-1)+fib(num-2);
    }
public static void main(String []args){
    Scanner sc=new Scanner(System.in);
    int num=sc.nextInt();
    System.out.print(fib(num));
}
}