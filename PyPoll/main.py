# Dependencies
import os
import csv

# Set paths for resource and output files
election_path = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join('Output', 'election_results.txt')

# Create a dictionary to be used for candidate name and vote count
election = {}

# Set variable total votes and initial value to zero
total_votes = 0

# Open data file
with open(election_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header
    header = next(csvreader)

    # Create a dictionary from file using column 3 as keys, using each name only once.
    # Count votes for each candidate as entries
    # Keep a total vote count by counting up 1 for each loop (# of rows w/o header)
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] in election.keys():
            election[row[2]] = election[row[2]] + 1
        else:
            election[row[2]] = 1
 
# Create empty list for candidates and their vote count
candidates = []
votes = []

# Create lists to hold dictionary keys (candidates) and values (votes) 
for candidate, vote in election.items():
    candidates.append(candidate)
    votes.append(vote)

# Create vote percent list
vote_percent = []
for n in votes:
    vote_percent.append(round(n/total_votes*100, 1))

# Zip candidates, votes, vote_percent into tuples
clean_data = list(zip(candidates, votes, vote_percent))

# Create winner_list for the winners
winner_list = []

for name in clean_data:
    if max(votes) == name[1]:
        winner_list.append(name[0])

# Make winner_list a str with the first entry
winner = winner_list[0]

# Run if there is a tie to add winners into a string separated by commas
if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]

# Print to file


with open(output_path, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in clean_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

#prints file to terminal
with open(output_path, 'r') as readfile:
    print(readfile.read())