def solution(numbers):
    if sum(numbers) == 0 :
        return "0"
    else :
        numbers = list(map(str, numbers))
        numbers.sort(key = lambda x : (x[0], x[1 % len(x)], x[2 % len(x)], x[3 % len(x)]), reverse = True)

        return ''.join(numbers)