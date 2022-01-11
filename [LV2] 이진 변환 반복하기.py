from collections import Counter

def solution(s):
    count = 0
    turn = 0
    while s != "1" :
        turn += 1
        count += Counter(s)["0"]
        s = s.replace("0", "")
        s = bin(len(s))[2:]
    
    return [turn, count]