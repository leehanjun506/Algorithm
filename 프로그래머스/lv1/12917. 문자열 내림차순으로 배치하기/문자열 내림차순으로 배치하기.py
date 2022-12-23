def solution(s):
    # print(ord('Z'))
    # print(ord('b'))
    s = [i for i in s]
    s.sort(reverse=True)
    return "".join(s)