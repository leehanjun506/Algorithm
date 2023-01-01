def solution(s):
    ans = len(s)
    for i in range(1,len(s)//2+1):# 자르는 단위
        a = ''
        count = 1
        tmp = s[0:i] 
        for j in range(i,len(s),i):
            if s[j:j+i] == tmp:
                count+=1
            else:
                if count>=2:
                    a += str(count)+tmp
                else:
                    a += tmp
                count = 1
                tmp = s[j:j+i]
                
        if count>=2:
            a+=str(count)+tmp
        else:
            a+=tmp
        ans = min(ans,len(a))
                
    return ans