# importing modules and saying where file is located
import os
import csv
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Establishing initital variables and their values
total_months = 0
total_net = 0
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999]

# Reading in the csv file
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
          
    # Extracting the header row
    csv_header = next(csv_reader)
    
   # Skipping to the next row in the csv file, being Jan-2010.
   # Then setting Jan-10 profit figure as the initial value for 'previous_value' which I will use when calcuating the change from month to month.
    first_row = next(csv_reader)
    previous_value = int(first_row[1])
    
    # Establishing the initial value for total months and total net to include Jan-10
    total_months += 1
    total_net += int(first_row[1])
       
    # Looping through the rows in the csv file
    for row in csv_reader:
        # Setting which columns date and profit and loss are
        date = row[0]
        profit_loss = row[1]

        # Calcuating the total number of months
        total_months += 1
          
        # Calculating the total profit
        total_net += int(profit_loss)
       
        # Calculating the net change and appending it to the list called 'net change list'
        net_change = int(row[1]) - previous_value
        net_change_list.append(net_change)
        # Updating the previous_value field to be equal to the profit/loss value of the current row
        previous_value = int(row[1])
                
        # Calcuating the average change in profit
        average_profit_change = sum(net_change_list) / len(net_change_list)

        # Checking whether the row has had the greatest increase
        # If it has, it's net change and date are assigned to the field 'greatest_increase'
        if net_change > greatest_increase[1]:
            greatest_increase[0] = date
            greatest_increase [1] = net_change

        # Checking whether the row has had the greatest net decrease
        # If it has, it's net change and date are assigned to the field 'greatest_decrease'
        if net_change < greatest_decrease[1]:
            greatest_decrease [0] = date
            greatest_decrease [1] = net_change

output_text = (f"Financial Analysis\n"
f"-----------------------------\n"
f"Total Months: {str(total_months)}\n"
f"Total: ${str(total_net)}\n"
f"Average : ${round(average_profit_change,2)}\n"
f"Greatest Increase in Profits: {greatest_increase[0]} (${str(greatest_increase[1])})\n"
f"Greatest Decrease in Profits: {greatest_decrease[0]} (${str(greatest_decrease[1])})\n")

# Printing results to the terminal
print(output_text)

# Noting file path for the output text file and and printing the results to it
output_file = os.path.join("analysis", "output.txt")
with open(output_file, "w") as file:
        file.write(output_text)


