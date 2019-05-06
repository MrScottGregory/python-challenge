# import os and csv modules
import os
import csv

# connect to data
budget_data = os.path.join('..', 'Resources', 'homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

with open(budget_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # set variable to hold row count and start at 0
    rows_count = 0
    # set variable to hold net_profit so we can sum it by row
    net_profit = 0
    # establish a list to hold all the values in the month column
    month_list = []
    # establish a list to hold all the values in the profit column
    profit_list = []

# TASK #1 calculate total number of months included in the dataset
    # loop through each row
    for row in csvreader:
        # add 1 for each row in loop (total # of row = total months)
        rows_count = rows_count + 1

# TASK #2 calculate net total amount of "Profit/Losses" over the entire period
        # sum column 2
        net_profit = net_profit + int(row[1])

# TASK # 3 calculate average of the changes in "Profit/Losses" over the entire period
        # casting as float allows us to have points after decimal (more accurate for avg)
        avg_profit = float(net_profit / rows_count)  

# TASK # 4 identify the greatest increase in profits (date and amount) over the entire period
        # append all of the values in profit column to make an indexed list
        profit_list.append(int(row[1]))
        # append all of the values in month column to make an indexed list
        month_list.append(row[0])
        # use max function to search for max value in profit list
        max_profit = max(profit_list)
        # use index function to grab the index number for the max value
        max_index = profit_list.index(max_profit)
        # search for the month that corresponds to that same index number in the month list
        max_month = month_list[max_index]
       

# TASK # 5 identify the greatest decrease in losses (date and amount) over the entire period
        min_profit = min(profit_list)
        min_index = profit_list.index(min_profit)
        min_month = month_list[min_index]

# TASK #6 print analysis summary to terminal    
    print("Financial Analysis")
    print("-------------------------------------------------------------------")
    print(f'Total Months: {rows_count}')
    print(f'Total: ${net_profit}')
    # the :.2F code tells python to limit the number (a float, see above) to just 2 decimal places
    print(f'Average Change: ${avg_profit:.2F}')
    print(f'Greatest Increase in Profits: {max_month} (${max_profit})')
    print(f'Greatest Decrease in Proftis: {min_month} (${min_profit})')


# TASK #7 export results to a text file

file = open("PyBankResults.txt", "w+")

file.write("Financial Analysis\n")
file.write("-------------------------------------------------------------------\n")
file.write(f'Total Months: {rows_count}\n')
file.write(f'Total: ${net_profit}\n')
file.write(f'Average Change: ${avg_profit:.2F}\n')
file.write(f'Greatest Increase in Profits: {max_month} (${max_profit})\n')
file.write(f'Greatest Decrease in Proftis: {min_month} (${min_profit})')