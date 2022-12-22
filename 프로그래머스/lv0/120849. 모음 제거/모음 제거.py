def solution(my_string):
    answer = ''
    ex = ['a','e','i','o','u']
    for i in ex:
        my_string = my_string.replace(i,'')
    return my_string