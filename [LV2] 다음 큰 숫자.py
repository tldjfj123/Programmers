from collections import Counter

def solution(n):
    max = 1000000
    num_of_one = Counter(bin(n)[2:])['1']
    
    for i in range(n+1, max) :
        if Counter(bin(i)[2:])['1'] == num_of_one :
            return i