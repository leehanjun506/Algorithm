#프로그래머스https://programmers.co.kr/learn/courses/30/lessons/60060
'''
효율성 실패 case
def checkwords(len_new_query,query,words,flag):
    ans = 0
    for word in words:
        if len(word) != len(query):
            continue
        if flag == True:
            new_word = word[len(word)-len_new_query:]
            new_query = query[len(query)-len_new_query:]
            if new_word == new_query:
                ans+=1
        else:
            new_word = word[:len_new_query]
            new_query = query[:len_new_query]
            if new_word == new_query:
                ans+=1
    return ans
        
    
def solution(words, queries):
    result = []
    keyword = '?'
    for query in queries:
        len_q = len(query)
        keyword_count = query.count(keyword)
        len_new_query = len_q-keyword_count
        if query[0] == '?':
            ans = checkwords(len_new_query,query,words,True) # 접두사에 존재
        else:
            ans = checkwords(len_new_query,query,words,False) # 접미사에 존재
        result.append(ans)
    return result
'''
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