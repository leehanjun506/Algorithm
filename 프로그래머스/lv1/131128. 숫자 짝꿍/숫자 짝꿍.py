def solution(X, Y):
    x = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    y = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    for i in X:
        x[i] += 1
    for i in Y:
        y[i] += 1
    num = "987654321"
    ans = ''
    for i in num:
        if x[i] >0 and y[i] >0:
            val = min(x[i],y[i])
            ans+=(i*val)
    ans2 = ''
    if x['0'] > 0 and y['0']>0:
        val = min(x['0'],y['0'])
        ans2+= '0'*val
    
    if ans == '' and ans2 == '':
        return '-1'
    elif ans == '' and ans2 != '':
        return '0'
    else:
        return ans+ans2