# importing data file
import os
import csv

from collections import Counter

election_csv = os.path.join('Resources', 'election_data.csv')

total_votes = 0

# Candidate list
candidate_list = []
candidate_counts = {}


# Read the csv file
with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
          
    # Read the header row first 
    csv_header = next(csv_reader)
   
    for row in csv_reader:
        # Calculate total number of votes
        total_votes += 1

        # Checking whether the current candidate is in the candidate list, if not it adds it to the list
        current_candidate = row[2]
        if current_candidate not in candidate_list:
            candidate_list.append(current_candidate)

            # sets the count value for the candidate as zero (will do this for those candidates that get appended to the list)
            candidate_counts[current_candidate] = 0
        
        # my key for the dictionary is 'current_candidate' each time the candidate comes up it will add to the count for that candidate
        candidate_counts[current_candidate] += 1

# Saving the txt output file path
output_file = os.path.join("analysis", "output.txt")

output_1 = (f"Election Results\n"
f"--------------------\n"
f"Total Votes: {total_votes}\n"
f"--------------------\n")

# Printing results to the terminal
print(output_1)

# Printing the results to a text file
with open(output_file, "a") as file:
    file.write(output_1)
    # file.write(f"{output_1}")
    
vote_count = 0
# Loop through the 3 candidates in the candidate list
for candidate in candidate_list:
    candidate_percent = round(candidate_counts[candidate]/total_votes * 100,3)
    output_2 = (f"{candidate}: {candidate_percent}% ({candidate_counts[candidate]})\n")
    
    # Printing results to the terminal
    print(output_2)

    # Printing the results to the text file
    with open(output_file, "a") as file:
        file.write(output_2)
        # file.write(f"{output_2}")
       
    if vote_count < candidate_counts[candidate]:
        winner = candidate
        vote_count = candidate_counts[candidate]

output_3 = (f"--------------------\n"
f"Winner: {winner}\n"
f"--------------------\n")

# Printing results to the terminal
print(output_3)

# Printing results to the text file
with open(output_file, "a") as file:
        file.write(f"{output_3}")
