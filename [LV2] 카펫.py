import math

def solution(brown, yellow):
    sum = brown + yellow
    arr = []
    
    for i in range(3, sum+1) :
        if sum % i == 0 :
            if i <= sum // i :
                arr.append((sum // i , i))
            else :
                break
    print(arr)
    
    if len(arr) == 1 :
        return list(arr[0])
    else :
        for i in arr :
            b = 0
            y = 0

            for j in range(i[0]) :
                if j == 0 or j == i[0]-1 :
                    b += i[1]
                else :
                    b += 2
                    y += (i[1] - 2)
                    
            if b == brown and y == yellow :
                return [i[0], i[1]]