def solution(n, arr1, arr2):
    ans1 = []
    ans2 = []
    def sol(num,length):
        ans = ''  
        while length != 0:
            val = num // 2**(length-1) 
            ans+=str(val) 
            num %= 2**(length-1) 
            length-=1
        return ans

    for i in range(n):
        ans1.append(sol(arr1[i],n))
        ans2.append(sol(arr2[i],n))
    ans3 = []
    for i in range(n):
        v = ''
        for j in range(n):
            if ans1[i][j] == '0' and ans2[i][j] == '0':
                v+=' '
            else:
                v+='#'
        ans3.append(v)
    return ans3