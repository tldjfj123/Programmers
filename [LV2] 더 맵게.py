import heapq

def solution(scoville, K) :
    heapq.heapify(scoville)
    count = 0
    
    while scoville[0] < K :
        count += 1
        tmp = heapq.heappop(scoville) + (2 * heapq.heappop(scoville))
        heapq.heappush(scoville, tmp)
        
        if len(scoville) <= 1 :
            if scoville[0] < K :
                return -1
        
    
    return count