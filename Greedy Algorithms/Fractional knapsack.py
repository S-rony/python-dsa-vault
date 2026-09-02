def fractional_knapsack(item_wt, price, capacity):
    n = len(item_wt)
    items = [(price[i], item_wt[i], price[i]/item_wt[i]) for i in range(n)]

    for i in range(n):
        for j in range(i+1,n):
            if items[i][2] < items[j][2]:
                items[i], items[j] = items[j], items[i]

    profit = 0
    for price, item_wt, per_kg_price in items:
        if capacity >= item_wt:
            capacity = capacity - item_wt
            profit = profit + price
        else:
            profit = profit + per_kg_price * capacity
            break

    print("Total Profit = ", profit)

price = [21,24,12,40,30]
item_wt = [7,4,6,5,6]
capacity = 20
fractional_knapsack(item_wt, price, capacity)

