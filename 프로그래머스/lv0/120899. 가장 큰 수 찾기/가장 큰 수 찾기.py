def solution(array):
    answer = [i for i in range(len(array)) if array[i] == max(array)]
    m = max(array)
    answer.append(m)
    return answer[::-1]
