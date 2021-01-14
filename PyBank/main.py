#import modules
import os
import csv

#make filepath for input
filepath_input = os.path.join("resources","budget_data.csv")

#initialise lists
months = []
profit = []
profit_change = [0]

with open(filepath_input, 'r') as budget_data_file:
    data = csv.reader(budget_data_file, delimiter = ",")
    data_header = next(data)
    
    #extract columns
    for row in data:
        months.append(row[0])
        profit.append(int(row[1]))

    #populate profit change list
    for i in range(1,len(profit)):
        profit_change.append(profit[i]-profit[i-1])

#find index of max/min profit change so we can output respective month
max_profit_change_index = profit_change.index(max(profit_change))
min_profit_change_index = profit_change.index(min(profit_change))

print("--------------------------------------------------")
print("Financial Analysis")
print("--------------------------------------------------")
print(f"Total Months: {len(months)}")
print(f"Total Profit: ${sum(profit)}")
print(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profit: {months[max_profit_change_index]} (${max(profit_change)})")
print(f"Greatest Decrease in Profit: {months[min_profit_change_index]} (${min(profit_change)})")

#write into output file
filepath_output = os.path.join("analysis","budget_analysis.txt")

with open(filepath_output, "w", newline = "") as analysis:

    analysis.write("-------------------------------------------------\n")
    analysis.write("Financial Analysis\n")
    analysis.write("-------------------------------------------------\n")
    analysis.write(f"Total Months: {len(months)}\n")
    analysis.write(f"Total Profit: ${sum(profit)}\n")
    analysis.write(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}\n")
    analysis.write(f"Greatest Increase in Profit: {months[max_profit_change_index]} (${max(profit_change)})\n")
    analysis.write(f"Greatest Decrease in Profit: {months[min_profit_change_index]} (${min(profit_change)})\n")