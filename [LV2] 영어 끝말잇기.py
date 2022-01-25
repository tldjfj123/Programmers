import math

def solution(n, words):
    count = 0
    used = []
    
    for i in range(len(words)) :
        count += 1
        if i == 0 :
            used.append(words[i])
        else :
            if words[i-1][-1] == words[i][0] :
                if words[i] in used :
                    break
                else :
                    used.append(words[i])
            else :
                break
    else :
        return [0, 0]
    
    if count % n == 0 :
         return [n, math.ceil(count / n)]
    return [count % n,  math.ceil(count / n)] 