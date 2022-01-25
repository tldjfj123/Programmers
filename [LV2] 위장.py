def solution(clothes):
    table = dict()
    for c in clothes :
        if len(table.keys()) == 0 :
            table[c[1]] = 1
        else :
            if c[1] in table.keys() :
                table[c[1]] = table[c[1]]+1
            else :
                table[c[1]] = 1
    
    res = 1
    fin = list(table.values())
    
    for f in fin :
        res *= (f + 1)
    
    return res-1   