def solution(s):
    s = list(s)
    h = True
    
    for i in range(len(s)) :
        if ord(s[i]) == 32 :
            h = True
        else :
            if h == True :
                if ord(s[i]) in range(97, 123) :
                    s[i] = chr(ord(s[i]) - 32)
                h = False
            else :
                if ord(s[i]) in range(65, 91) :
                    s[i] = chr(ord(s[i]) + 32)
                    
    return ''.join(s)