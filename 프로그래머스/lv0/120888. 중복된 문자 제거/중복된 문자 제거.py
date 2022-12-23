def solution(my_string):
    old = [i for i in my_string]
    new = []
    for i in old:
        if i not in new:
            new.append(i)
    
    return "".join(new)