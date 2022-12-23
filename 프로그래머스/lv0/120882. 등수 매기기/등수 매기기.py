def solution(score):
    avg = [sum(i)/2 for i in score]
    avg.sort(reverse=True)
    dic = dict()
    for i,v in enumerate(avg):
        if v not in dic.keys():
            dic[v] = i+1
    return [dic[sum(i)/2] for i in score]