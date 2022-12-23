import java.util.Arrays;
class Solution {
    int gcd(int x,int y){
        if(x%y==0)
            return y;
    return gcd(y,x%y);
    }
    int lcd(int x,int y){
        return x*y/gcd(x,y);
    }
    public int solution(int[] arr) {
        Arrays.sort(arr);
        int answer = arr[0];
        for(int i=0;i<arr.length;i++){
            answer=lcd(answer,arr[i]);
        }
        return answer;
    }
}