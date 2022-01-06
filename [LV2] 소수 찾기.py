from itertools import permutations

def prime(n : int) -> bool :
    m = int(n ** 0.5)
    if n <= 1 :
        return False
    for i in range(2, m+1) :
        if n % i == 0 :
            return False
    return True

def solution(numbers):
    n = list(numbers)
    m = []
    for i in range(1, len(n)+1) :
        tmp = list(set(list(permutations(n, i))))
        for t in tmp :
            m.append(t)
        
    m = list(set(list(map(lambda x : int(''.join(x)), m))))
    
    count = 0
    for i in m :
        if prime(i) == True :
            count += 1
    
    return count