from math import gcd

def lcm(a : int, b : int) -> int :
    return (a * b) // gcd(a, b)

def solution(arr):
    res = 1
    if len(arr) == 1 :
        return arr[0]
    else :
        for i in range(len(arr)) :
            res = lcm(arr[i], res)  
    
    return res