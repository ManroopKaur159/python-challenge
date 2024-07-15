#import os module and csv
import os
import csv

# The path for the budget data CSV file is set
budget_data_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

# Then initializing variables
total_months = 0
net_total = 0
prev_profit = 0
profit_changes = []
months = []

# Instructions to read the csv file
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Reading the header row
    csv_header = next(csvreader)

    # In the CSV file loop through row
    for row in csvreader:
        # Total number of months has to be counted
        total_months += 1

        # Net total amount of "Profit/Losses" calculation
        net_total += int(row[1])

        # Change in profit from the previous month calculation
        profit_change = int(row[1]) - prev_profit
        prev_profit = int(row[1])
        profit_changes.append(profit_change)
        months.append(row[0])

# Average change in profits calculation
average_change = sum(profit_changes[1:]) / len(profit_changes[1:])

# Greatest increase and decrease in profits
max_increase = max(profit_changes)
max_decrease = min(profit_changes)
max_increase_month = months[profit_changes.index(max_increase)]
max_decrease_month = months[profit_changes.index(max_decrease)]

# Displaying the analysis results on the terminal
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})")

# Exporting the analysis results to a text file in analyis folder called financial_analysis.txt
output_file = os.path.join("PyBank", "analysis", "financial_analysis.txt")
with open(output_file, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})\n")