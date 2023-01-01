from itertools import permutations
def solution(babbling):
    pron = ['aya',"ye","woo","ma"]
    ban = []
    for i in permutations(pron,2):
        ban.append("".join(i))
    for i in permutations(pron,3):
        ban.append("".join(i))
    for i in permutations(pron,4):
        ban.append("".join(i))
    answer = 0
    pron.extend(ban)
    for i in babbling:
        if i in pron:
            answer+=1
    return answer