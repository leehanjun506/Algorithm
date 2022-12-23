def solution(n, words):
    prev = words[0]
    num = 0
    turn = 0
    for i in range(1,len(words)):
        if prev[-1] == words[i][0] and words[i] not in words[:i]:
            prev = words[i]
            continue
        else:
            num = i%n+1
            turn = i//n+1
            return [num,turn]
    return [0,0]