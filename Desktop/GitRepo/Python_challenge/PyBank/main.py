#PyBank
#Import dependencies 
import os
import csv
import statistics as st
import pandas as pd
#Setting variables    
total_month = 0
total_profit =0
total_loss = 0
net_profit = total_profit + total_loss
average_change = []
count_row = 0
change_list = []
date_list = []

    
#setting up csv reader
csvpath = os.path.join("budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
#skipping header 
    next(csvreader, None)
    
#starting the for loop
    for row in csvreader:
#Counting the length of the period
        total_month += 1
#Setting a list of dates to refer to, when printing out the profit/losses
        date_list.append(row[0])
#Calculating the profit/losses
        money = int(row[1])
        if money > 0:
            total_profit += money
        elif money < 0:
            total_loss += money
        
#Calculating average change
        count_row += 1
        if count_row==1:
            pre_amt = float(row[1])
        elif count_row >1:
            change = float(row[1]) - pre_amt
            change_list.append(change)
            pre_amt = float(row[1])        
    total_change = sum(change_list)
    average_change = total_change/ (total_month - 1)
#Finding the index number for the max/min changes in the profit.
    date_profit = change_list.index(max(change_list))
    date_losses = change_list.index(min(change_list))
#printing the values
    print("Total months:", total_month)
    print("Total: $",(total_profit + total_loss))
    print("Average change in profit is ", round(average_change,2), " dollars.")
    print('The greatest increase in profit was ', max(change_list), ' on ', date_list[date_profit + 1])
    print('The greatest decrease in profit was ', min(change_list), ' on ', date_list[date_losses + 1])
#Printing out the result to a text file    
output_path = os.path.join("analysis.txt")
with open(output_path, "w+") as textfile:
    textfile.writelines("Financial Analysis" + '\n')
    textfile.writelines("Total months:" + str(total_month)+ '\n')
    textfile.writelines("Total: $"+ str(total_profit + total_loss)+ '\n')
    textfile.writelines("Average change in profit is " + str(round(average_change,2)) + " dollars."+ '\n')
    textfile.writelines('The greatest increase in profit was ' +  str(max(change_list)) + ' on ' + date_list[date_profit + 1]+ '\n')
    textfile.writelines('The greatest decrease in profit was ' + str(min(change_list)) + ' on ' + date_list[date_losses + 1]+ '\n')

    
    
    