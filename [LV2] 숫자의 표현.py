def solution(n) :
    count = 0
    sum = 0
    for i in range(1, n+1) :
        plus = i
        while i <= n :
            sum += plus
            plus += 1
            
            if sum == n :
                count += 1
                sum = 0
                plus = 1
                break
            elif sum > n :
                sum = 0
                plus = 1
                break

    return count