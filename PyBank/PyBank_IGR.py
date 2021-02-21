
#lets get started with PyBank!

import os
import csv

greatest_increase = ['', 0]
greatest_decrease = ['', 9999999999999999999]   
change_list = []
total_change = 0
months = [] 
total_m = 1
net_total= 0
file_to_output = os.path.join("budget_analysis.txt")


budget_csv = os.path.join('.','Resources','budget_data.csv')
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    first_row = next(csvreader)
    previous_row = int(first_row[1])
    net_total = int(first_row[1])
    
    for row in csvreader:

        net_total+=int(row[1])
        total_m = total_m+1
        current_value = int(row[1])
        
        change_value = int(current_value-previous_row)

        change_list.append(change_value)
        months.append(row[0])
        previous_row = int(row[1])

        total_change = total_change + change_value 
        if change_value > greatest_increase[1]:
           greatest_increase[0] = str(row[0])
           greatest_increase[1] = change_value


        if change_value < greatest_decrease[1]:
           greatest_decrease[0] = str(row[0])
           greatest_decrease[1] = change_value
		
    
        avg_change = total_change/len(months)
   
output = (
   f"\n Financial Analysis \n"
   f"------------------------------\n"
   f"Total Months: {total_m}\n"
   f"Total: ${net_total}\n"
   f"Average  Change: ${avg_change:.2f}\n"
   f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
   f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

with open(file_to_output, "w") as txt_file:
   txt_file.write(output)  

   file_to_output


