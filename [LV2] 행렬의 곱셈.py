def solution(arr1, arr2):
    res = []
    
    for i in range(len(arr1)) :
        res.append([])
        
        for j in range(len(arr2[0])) :
            sum = 0
            
            for k in range(len(arr1[i])) :
                sum += arr1[i][k] * arr2[k][j]
            
            res[i].append(sum)
            
    return res