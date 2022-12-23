def solution(my_string, num1, num2):
    s = [i for i in my_string]
    s[num1],s[num2] = s[num2],s[num1]  
    return "".join(s)
