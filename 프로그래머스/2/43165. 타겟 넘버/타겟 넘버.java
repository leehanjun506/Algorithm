import java.util.*;
// import java.io.*

class Solution {
    int answer;
    void dfs(int index, int value, int target, int[] numbers,int len){
        
        if (index == len-1) {
            if (value == target){
               answer+=1; 
            }
            return;
        
        }
        dfs(index+1,value+numbers[index+1],target,numbers,len);
        dfs(index+1,value-numbers[index+1],target,numbers,len);
        
    }
    public int solution(int[] numbers, int target) {
        int index = 0;
        int len = numbers.length;
        dfs(index,numbers[index],target,numbers,len);
        dfs(index,-numbers[index],target,numbers,len);
        return answer;
    }
    
}