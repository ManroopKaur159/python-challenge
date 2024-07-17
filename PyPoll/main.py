#import os module and csv
import os
import csv

# The path for the budget data CSV file is set
election_data_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

# Then we initialize the variables
candidate_votes = {}
candidates = []
total_votes = 0


# Instructions to read the csv file
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Reading the header row
    csv_header = next(csvreader)

    # In the CSV file loop through row
    for row in csvreader:
        # Total number of votes has to be counted
        total_votes += 1

        # Candidate's name
        candidate = row[2]

        # Add the candidate to the list if they are not already on it
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0

        # Increasing the candidate's vote count
        candidate_votes[candidate] += 1

# Percentage of votes each candidate won calculation
candidate_percentages = {}
for candidate in candidates:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100
    candidate_percentages[candidate] = percentage

# FInding out the winner as per the popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Displaying the analysis results on the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Exporting the analysis results 
# Saving results to a text file in analyis folder called election_results.txt
output_file = os.path.join("PyPoll", "analysis", "election_results.txt")
with open(output_file, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate in candidates:
        txtfile.write(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")