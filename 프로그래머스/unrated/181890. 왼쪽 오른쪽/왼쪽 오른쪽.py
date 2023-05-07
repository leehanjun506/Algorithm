def solution(str_list):
    s = ''.join(str_list)
    l = s.find('l')
    r = s.find('r')
    # print(l,r)
    if l == -1 and r == -1:
        return []
    if r == -1 and l != -1:
        if l == 0 :
            return []
        return str_list[:l]
    if l == -1 and r != -1:
        if r == len(str_list)-1 :
            return []
        return str_list[r+1:]
    if l<r:
        return str_list[:l]
    else:
        return str_list[r+1:]
