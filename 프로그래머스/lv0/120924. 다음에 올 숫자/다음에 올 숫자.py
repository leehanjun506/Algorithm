def solution(common):
    if common[1]*common[1] == common[0]*common[2] and 0 not in common:
        r = common[1]//common[0]
        return common[-1]*r
    if abs(common[1]-common[0]) == abs(common[2] - common[1]):
        d = common[1]-common[0]
        return common[-1]+d
    answer = 0
    return answer