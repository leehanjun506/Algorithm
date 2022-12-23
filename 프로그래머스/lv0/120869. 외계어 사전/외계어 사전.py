def solution(spell, dic):
    tag = [True]*len(dic)
    for i,v in enumerate(dic): 
        for j in spell:
            if j in v:
                continue
            else:
                tag[i] = False
    if True in tag:
        return 1
    else:
        return 2
