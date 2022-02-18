prices = [1,2,3,0,5]
def best_time_to_buy_stock(prices):
    count = 0
    sum = 0
    while count < len(prices):
        if prices[count] == prices[-1]:
            print(sum)
            return
        elif prices[count + 1] > prices[count]:
            sum += (prices[count + 1] - prices[count])
            count += 1
        else: 
            count += 1
        
    print(sum)
best_time_to_buy_stock(prices)