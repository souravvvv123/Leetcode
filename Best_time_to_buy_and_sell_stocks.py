prices = [3,4,22,11,7]
n = len(prices)
max_profit = 0

   
for i in range(n):
    for j in range(i + 1, n):
        profit = prices[j] - prices[i]
        if profit > max_profit:
            max_profit = profit

print(max_profit)
