def solution(polynomial):
    poly = polynomial.split(' + ')
    num = 0
    str_num = 0
    for i in poly:
        if 'x' not in i:
            num+= int(i)
        else:
            i = i.replace("x","")
            if i == '':
                i = 1
            str_num += int(i)
    str_x = str(str_num)+'x'
    if str_num == 1:
        str_x = 'x'
    if str_num == 0 and num == 0:
        return ''
    elif str_num == 0 and num != 0:
        return str(num)
    elif str_num != 0 and num == 0:
        return str_x
    else:
        return str_x+' + '+str(num)
        
