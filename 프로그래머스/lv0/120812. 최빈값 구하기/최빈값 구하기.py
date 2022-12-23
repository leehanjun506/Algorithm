from collections import Counter
def solution(array):
    c = Counter(array)
    mc = c.most_common()
    return -1 if len(mc) > 1 and mc[0][1] == mc[1][1] else mc[0][0]
