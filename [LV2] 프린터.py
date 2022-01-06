from collections import deque

def solution(p, l):
    p = deque(p)
    pointer = deque([False] * len(p))
    pointer[l] = True
    count = 0
    
    while 1 :
        if p[0] == max(p) :
            count += 1
            if pointer[0] == True :
                return count
            p.popleft()
            pointer.popleft()
        else :
            p.append(p.popleft())
            pointer.append(pointer.popleft())