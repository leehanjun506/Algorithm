answer = 0
def solution(numbers, target):
    def dfs(target,val,index):
        global answer
        index+=1
        if index == len(numbers):
            if val == target:
                answer+=1
            return
        dfs(target,val+numbers[index],index)
        dfs(target,val-numbers[index],index)
        
    dfs(target,numbers[0],0)
    dfs(target,-numbers[0],0)
    
    return answer