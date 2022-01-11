from itertools import product

def solution(word):
    res = []
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    for i in range(1, 6) :
        tmp = list(product(vowels, repeat = i))
        for t in tmp :
            res.append(''.join(t))
    
    res.sort()
    
    return res.index(word) + 1