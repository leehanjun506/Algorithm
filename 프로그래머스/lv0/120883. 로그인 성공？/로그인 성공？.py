def solution(id_pw, db):
    answer = ["fail"]*len(db)
    for i,v in enumerate(db):
        if v[0] == id_pw[0]:
            answer[i] = "wrong pw"
        if v[0] == id_pw[0] and v[1] == id_pw[1]:
            answer[i] = "login"
    
    if "login" in answer:
        return "login"
    elif "wrong pw" in answer:
        return 'wrong pw'
    else:
        return "fail"