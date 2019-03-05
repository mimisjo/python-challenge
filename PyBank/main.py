# Dependencies
import os
import csv

# Set paths for resource and output files
budget_path = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join('Output','pybank_results.txt')

# Create empty lists for month and revenue data
months = []
revenue = []
revenue_changes = []

# Create variables and set initial values
total_revenue = 0
previous_revenue = 0
revenue_change = 0
max_increase = 0
max_decrease = 0

# Open and read csv, skipping header
with open(budget_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Add data to months and revenue lists
    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))
        
        # Build out revenue change list
        revenue_change = int(row[1]) - previous_revenue
        revenue_changes.append(revenue_change)

# Count total months
total_months = len(months)
# print(total_months)

# Calculate average_change
average_change = round(sum(revenue_changes) / len(revenue_changes))
# print(average_change)

# Loop through revenue to calculate total revenue
for i in range(len(revenue)):
    # Add each revenue to total revenue
    total_revenue = total_revenue + revenue[i]
# print(total_revenue)

# Loop through revenue_changes to find greatest increase/decrease
    if revenue_changes[i] >= max_increase:
        max_increase = revenue_changes[i]
        max_increase_month = months[i]
    elif revenue_changes[i] <= max_decrease:
        max_decrease = revenue_changes[i]
        max_decrease_month = months[i]
# print(max_increase)
# print(max_decrease)

# opens the output destination in write mode and prints the summary
with open(output_path, 'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(total_months) + '\n')
    writefile.writelines('Total Revenue: $' + str(total_revenue) + '\n')
    writefile.writelines('Average Revenue Change: $' + str(average_change) + '\n')
    writefile.writelines('Greatest Increase in Revenue: ' + max_increase_month + ' ($' + str(max_increase) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Revenue: ' + max_decrease_month + ' ($' + str(max_decrease) + ')')

#opens the output file in r mode and prints to terminal
with open(output_path, 'r') as readfile:
    print(readfile.read())
