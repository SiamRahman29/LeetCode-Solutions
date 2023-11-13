def solution(amount, coins):
    table = [amount+1]*(amount+1)
    table[0] = 0
    for i in range(1,amount + 1):
        for c in coins:
            if i - c >= 0:
                table[i] = min(table[i],1 + table[i-c])
    return table[amount] if table[amount]!=amount+1 else -1