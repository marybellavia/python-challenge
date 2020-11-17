# Modules
import os
import csv

# Set path for file
budgetpath = os.path.join("Resources", "budget_data.csv")

# Specify the file to write to
output_path = os.path.join("output", "new.txt")

# setting all my variables
num_of_months = 0
total_profit_loss = 0
total_change = None
prev_row = 0
increase_num = 0
increase_mon = None
decrease_num = 0
decrease_mon = None

# opening the cvs file to work with
with open(budgetpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    # getting the header
    csv_header = next(csv_reader)

    # looping through my cvs file
    for row in csv_reader:
        # adding to the num_of_months variable for each loop
        num_of_months += 1
        
        # adding to profit/loss total
        total_profit_loss += int(row[1])

        # conditional to test if this is the first row of data or not
        if total_change != None:

            # getting a value for current row & calculating change
            current_row = int(row[1])
            change = current_row - prev_row

            # grabbing the greatest increase and decrease
            if change > increase_num:
                increase_num = change
                increase_mon = row[0]
            elif change < decrease_num:
                decrease_num = change
                decrease_mon = row[0]

            # adding up the change to my total change and resetting my prev_row
            total_change += change
            prev_row = int(row[1])  

        # this is here so I can start all my change stuff at the second row but grab my first prev_row
        else:
            prev_row = int(row[1])
            total_change = 0

    # calculating average change
    avg_change = round(total_change / (num_of_months-1),2)
    
    # printing to terminal
    print(f"""Financial Analysis
----------------------------
Total Months: {num_of_months}
Total: ${total_profit_loss}
Average  Change: ${avg_change}
Greatest Increase in Profits: {increase_mon} (${increase_num})
Greatest Decrease in Profits: {decrease_mon} (${decrease_num})""")

# printing to file, open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as newfile:

    newfile.write(f"""Financial Analysis
----------------------------
Total Months: {num_of_months}
Total: ${total_profit_loss}
Average  Change: ${avg_change}
Greatest Increase in Profits: {increase_mon} (${increase_num})
Greatest Decrease in Profits: {decrease_mon} (${decrease_num})""")
