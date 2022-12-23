def solution(arr):
    answer = []
    for i in range(len(arr)-1,0,-1):
        if arr[i] == arr[i-1]:
            arr.pop()
            if i == 1:
                answer.append(arr.pop())
        else:
            answer.append(arr.pop())
            if i == 1:
                answer.append(arr.pop())
    return answer[::-1]