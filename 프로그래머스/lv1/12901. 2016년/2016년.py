def solution(a, b):
    month = {1:"FRI",2:"MON",3:"TUE",4:"FRI",5:"SUN",6:"WED",7:"FRI",8:"MON",9:"THU",10:"SAT",11:"TUE",12:"THU"}
    date1 = {"MON":0,"TUE":1,"WED":2,"THU":3,"FRI":4,"SAT":5,"SUN":6}
    m = month[a]
    b %= 7
    n = date1[m]  
    b += (n-1) 
    b %= 7
    for i,v in date1.items():
        if v == b:
            result = i
    return result