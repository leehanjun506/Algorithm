count = 0
def solution(n):
    def dfs(x,y,n):
        global count
        if x<y: return
        if x == n and y == n:
            count+=1
            return
        if x>n or y>n: return
        dfs(x+1,y,n)
        dfs(x,y+1,n)
        
    dfs(0,0,n)
    return count