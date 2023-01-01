from bisect import bisect_right,bisect_left
array = [[] for _ in range(10001)]
reverse_array = [[] for _ in range(10001)]

def count_by_range(array,left_value,right_value):
    left_index = bisect_left(array,left_value)
    right_index = bisect_right(array,right_value)
    return right_index-left_index
def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)
        reverse_array[len(word)].append(word[::-1])
    
    for i in range(10001):
        array[i].sort()
        reverse_array[i].sort()
    
    for query in queries:
        if query[0] != '?':
            ans = count_by_range(array[len(query)],query.replace('?','a'),query.replace('?','z'))
            answer.append(ans)
        else:
            ans = count_by_range(reverse_array[len(query)],query[::-1].replace('?','a'),query[::-1].replace('?','z'))
            answer.append(ans)
    
    return answer