def solution(num_list):
    odd = 0
    even = 0
    for i,v in enumerate(num_list):
        if i%2 == 0:
            odd+=v
        else:
            even+=v
    if odd>even:
        result = odd
    else:
        result = even
    return result