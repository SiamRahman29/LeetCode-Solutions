def solution(prices):
    profit = 0
    left = 0
    right = 1
    while(right < len(prices)):
        profitNow = prices[right] - prices[left]
        if profitNow <= 0:
            left = right
            right += 1
                
        else:
            right += 1
            profit = max([profit,profitNow])
        
    return profit