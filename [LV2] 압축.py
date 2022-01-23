msg = 'ABABABABABABABAB'

def solution(msg):
    table = dict()
    res = []

    idx = 1
    for i in range(65, 91) :
        table[chr(i)] = idx
        idx += 1
    
    length = 1
    while len(msg) != 0 :
        print(res)
        if msg[:length] in table.keys() and msg[:length+1] not in table.keys() :
            res.append(table[msg[:length]])
            table[msg[:length+1]] = max(table.values())+1
            msg = msg[length:]
            length = 1
        else :
            if msg in table.keys() :
                res.append(table[msg])
                msg = ""
            length += 1
    return res
solution(msg)
         