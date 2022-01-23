def solution(phone_book):
    pb = sorted(phone_book)
    for i in range(len(pb)-1) :
        if len(pb[i]) < len(pb[i+1]) :
            if pb[i+1][:len(pb[i])] == pb[i] :
                return False
    return True