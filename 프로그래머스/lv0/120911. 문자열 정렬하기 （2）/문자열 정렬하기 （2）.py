def solution(my_string):
    my_string = my_string.lower()
    s = [i for i in my_string]
    s.sort()
    return "".join(s)