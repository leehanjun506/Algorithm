from itertools import combinations

def solution(relation):
    tup_len = len(relation) # 6
    att_len = len(relation[0]) # 4
    comb_result = []
    for i in range(att_len):
        comb = [j+1 for j in range(att_len)]
        comb = list(combinations(comb,i+1))
        comb_result.extend(comb)
    ans = []    
    set_com = []
    for i in comb_result:
        x = set()
        i_set = set(i)
        for j in range(tup_len):
            y = []
            for k in i:
                y.append(relation[j][k-1])
            x.add(tuple(y))
        if len(x) == tup_len:
            set_com.append(i_set)
    for i in range(len(set_com)-1,-1,-1):
        tag = 0
        for j in range(i-1,-1,-1):
            if set_com[i].issuperset(set_com[j]):
                tag = 1
                break
        if tag == 0:
            ans.append(set_com[i])
    

        
    return len(ans)
