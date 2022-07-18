# https://programmers.co.kr/learn/courses/30/lessons/60058
# 값 자체를 변수에 저장하지말고 return하면서 나중에 더해지는 알고리즘 필요
# 문자열 파싱능력 부족!

def solution(p):
    
    def correct(string):
        if len(string) == 0:
             return True
        list = []
        if string[0] == ')':
            return False
        else:
            list.append(string[0])
        for i in range(1,len(string)):
            if string[i] == '(':
                list.append(string[i])
            else:
                if len(list) == 0:
                    return False
                list.pop()
        if len(list) != 0:
            return False
        return True
    def uandv(string):
        x,y=0,0
        u_list = []
        v_list = []
        for i in range(len(string)):
            if string[i]=='(':
                x+=1
            else:
                y+=1
            if x==y:
                u_list = string[0:i+1]
                v_list = string[i+1:]
                return u_list,v_list
    def recursive(p):
        if len(p) == 0:
            return p
        u,v = uandv(p) # )(  ,  ' '
        if correct(u) == True:
            if correct(v)==True:
                u+=v
                return u
            else:
                return u+recursive(v)
        else:
            empty = ''
            empty +='('
            empty +=recursive(v)
            empty +=')'
            u=u[1:]
            u=u[:-1]
            u=u.replace('(','x')
            u=u.replace(')','y')
            u=u.replace('x',')')
            u=u.replace('y','(')
            return empty+u
            
    ans = recursive(p)
            
    return ans

print(solution("()))((()"))