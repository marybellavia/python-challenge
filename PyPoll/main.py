# Modules
import os
import csv

# Set path for file
electionpath = os.path.join("Resources", "election_data.csv")

# Specify the file to write to
output_path = os.path.join("output", "results.txt")

# opening the cvs file to work with
with open(electionpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    # getting the header and skipping header row
    csv_header = next(csv_reader)

    # setting variables
    num_votes = 0
    candidates_dict = {}

    # iterating through the data in the cvs file
    for row in csv_reader:
        
        # counting number of votes
        num_votes += 1

        # conditional for to add candidates to dictionary
        if row[2] not in candidates_dict:
            # the key is their name and the value is the count for their votes
            candidates_dict[row[2]] = 1
        # if they are already in the dictionary
        else:
            # getting old vote count from dictionary
            old_count = candidates_dict[row[2]]
            # creating new vote count
            new_count = old_count + 1
            # reassigning the new vote count as the value to that key / candidate
            candidates_dict[row[2]] = new_count

    # finding popular vote winner
    winner = max(candidates_dict, key=candidates_dict.get)

    # printing results in terminal
    print(f"""Election Results
-------------------------
Total Votes: {num_votes}
-------------------------""")
    # printing results by looping through dicitonary in terminal
    for key in candidates_dict:
        print(f"{key}: {round(((candidates_dict[key] / num_votes)*100),3)}% ({candidates_dict[key]})")
    # final print of popular vote winner in terminal
    print(f"""-------------------------
Winner: {winner}
-------------------------""")

# writing in file, open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as newfile:

    # writing to the file
    newfile.write(f"""Election Results
-------------------------
Total Votes: {num_votes}
-------------------------
""")
    for key in candidates_dict:
        newfile.write(f"""{key}: {round(((candidates_dict[key] / num_votes)*100),3)}% ({candidates_dict[key]})
""")
    
    newfile.write(f"""-------------------------
Winner: {winner}
-------------------------""")

