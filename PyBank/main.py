import os
import csv

filepath = os.path.join("resources","budget_data.csv")

with open(filepath, 'r') as budget_data_file:
    data = csv.reader(budget_data_file, delimiter = ",")
    data_header = next(data)
    
    months = []
    profit = []
    profit_change = [0]

    for row in data:
        months.append(row[0])
        profit.append(int(row[1]))
    
    for i in range(1,len(profit)):
        profit_change.append(profit[i]-profit[i-1])

    max_profit_change_index = profit_change.index(max(profit_change))
    min_profit_change_index = profit_change.index(min(profit_change))

    print("Financial Analysis")
    print("---------------------------------")
    print(f"Total Months: {len(months)}")
    print(f"Total Profit: ${sum(profit)}")
    print(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
    print(f"Greatest Increase in Profit: {months[max_profit_change_index]} (${max(profit_change)})")
    print(f"Greatest Decrease in Profit: {months[min_profit_change_index]} (${min(profit_change)})")
    