from collections import deque

def solution(s):
    s = deque(list(s))
    count = 0
    res = 0
    open = ['(', '{', '['] 
    close = [')', '}', ']']
    
    if len(s) == 1 :
        return 0
            
    while count != len(s) :
        stack = []

        for i in s :
            if len(stack) == 0 :
                if i in open :
                    stack.append(i)
                else :
                    break
            else :
                if i in close :
                    if ord(i) == 41 :
                        if ord(stack[-1]) == 40 :
                            stack.pop()
                        else :
                            break
                    elif ord(i) == 125 :
                        if ord(stack[-1]) == 123 :
                            stack.pop()
                        else :
                            break
                    else :
                        if ord(stack[-1]) == 91 :
                            stack.pop()
                        else :
                            break
                else :
                    stack.append(i)
        else :
            if len(stack) == 0 :
                res += 1
        
        s.append(s.popleft())
        count += 1
        
    return res