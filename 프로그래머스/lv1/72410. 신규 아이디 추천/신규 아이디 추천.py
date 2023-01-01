def solution(new_id):
    
    exceptions = []
    for i in '~!@#$%^&*()=+[{]}:?,<>/':
        exceptions.append(i)
    new_id = new_id.lower()
    for i in exceptions:
        new_id = new_id.replace(i,'')
    new = new_id.split('.')
    new_id = ''
    for i in range(len(new)):
        if new[i] == '':
            continue
        else:
            if new_id == '':
                new_id += new[i]
            else:
                if new_id == '':
                    new_id+=new[i]
                else:
                    new_id+='.'+new[i]
    if new_id == '':
        new_id+='a'
    if len(new_id)>=16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    if len(new_id)<=2:
        while(len(new_id)<3):
            new_id+=new_id[-1]
        
    return new_id