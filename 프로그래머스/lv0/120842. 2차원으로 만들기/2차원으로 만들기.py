def solution(num_list, n):
    answer = [[0]*n for i in range(len(num_list)//n)]
    for i,v in enumerate(num_list):
        row = i//n
        answer[row][i%n] = v
    return answer