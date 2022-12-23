def solution(array):
    answer = 0
    array = list(map(str,array))
    s = "".join(array)
    print(s)
    for i in s:
        if i == '7':
            answer+=1
    return answer