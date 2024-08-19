def solution(num_list):
    multi = 1
    for i in num_list:
        multi *= i
    return 1 if multi < sum(num_list)**2 else 0