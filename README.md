PyBank
First we import the os to handle file paths and csv module to read csv files
import os
import csv
Then we set up a path for the csv file
budget_data_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

After that we declare all the variables
total_months = 0
profit_changes = []
months = []
net_total = 0
prev_profit = 0

Then we give instructions to read the csv file and skip the header
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader
  We count the months and update net total amount of "Profit/Losses"
  total_months += 1
        net_total += int(row[1])
  After that we calculate the changes and track months.
  The profit change is calculated and added to profit_changes if there is a previous month's profit/loss to compare.
The average change is calculated by adding all changes and dividing by the number of changes.
The maximum and minimum changes are found using max() and min().
Months for the greatest increase and decrease are identified.
Results are printed on terminal.
Then the results are saved in a text file called financial_analysis.txt

PyPoll
First we import the os to handle file paths and csv module to read csv files
import os
import csv
Then we set up a path for the csv file
election_data_csv = os.path.join("PyPoll", "Resources", "election_data.csv")
Decalre the variables
candidate_votes = {}
candidates = []
total_votes = 0
Then we give instructions to read the csv file and skip the header
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
  Total number of votes are counted after that we get the candidates name 
  If the candidate in not on list add them to list
  After that increase the vote count of the  candidate
  Percentage of votes for each candidate is calculated
  Printing the results to the terminal.
  Then the results are saved in a text file called election_results.txt
