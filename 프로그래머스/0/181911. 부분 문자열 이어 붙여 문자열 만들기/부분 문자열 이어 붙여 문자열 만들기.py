def solution(my_strings, parts):
    answer = ''
    for i,v in enumerate(my_strings):
        answer+=v[parts[i][0]:parts[i][1]+1]
    return answer